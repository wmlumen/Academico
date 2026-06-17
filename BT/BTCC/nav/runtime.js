(function() {
  'use strict';

  var API_STATE = '/api/state';
  var SAVE_TIMER = null;
  var SAVE_DELAY = 150;
  var saveEnabled = true;

  /* ---- Computar base path desde la ubicacion de runtime.js ---- */
  function getDataBase() {
    var scripts = document.getElementsByTagName('script');
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].src || '';
      if (src.indexOf('runtime.js') !== -1) {
        // runtime.js esta en nav/, los datos estan en ../data/
        return src.substring(0, src.lastIndexOf('/') + 1) + '../';
      }
    }
    // Fallback: usar ruta relativa al documento actual
    return '';
  }

  var DATA_BASE = getDataBase();

  function resolvePath(path) {
    // Si comienza con /, se resuelve contra DATA_BASE (GitHub Pages compatible)
    if (path.charAt(0) === '/') {
      return DATA_BASE + path.substring(1);
    }
    return path;
  }

  function xhr(method, url) {
    try {
      var req = new XMLHttpRequest();
      req.open(method, resolvePath(url), false);
      req.send(null);
      if (req.status >= 200 && req.status < 300) return req.responseText;
    } catch (e) {}
    return null;
  }

  function loadStateSnapshot() {
    var raw = xhr('GET', API_STATE);
    if (!raw) return {};
    try {
      return JSON.parse(raw) || {};
    } catch (e) {
      return {};
    }
  }

  function currentSnapshot() {
    var data = {};
    for (var i = 0; i < localStorage.length; i++) {
      var key = localStorage.key(i);
      data[key] = localStorage.getItem(key);
    }
    return data;
  }

  function persistSnapshot() {
    if (!saveEnabled) return;
    try {
      fetch(resolvePath(API_STATE), {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(currentSnapshot())
      }).catch(function() {});
    } catch (e) {}
  }

  function schedulePersist() {
    if (!saveEnabled) return;
    clearTimeout(SAVE_TIMER);
    SAVE_TIMER = setTimeout(persistSnapshot, SAVE_DELAY);
  }

  function hydrateStorage() {
    var fileData = loadStateSnapshot();
    var localData = currentSnapshot();
    var merged = {};
    var key;

    for (key in fileData) merged[key] = fileData[key];
    for (key in localData) {
      if (!(key in merged)) merged[key] = localData[key];
    }

    saveEnabled = false;
    try {
      for (key in merged) {
        localStorage.setItem(key, merged[key]);
      }
    } finally {
      saveEnabled = true;
    }

    if (Object.keys(localData).length && Object.keys(fileData).length !== Object.keys(merged).length) {
      schedulePersist();
    }
  }

  function patchStorage() {
    var originalSetItem = Storage.prototype.setItem;
    var originalRemoveItem = Storage.prototype.removeItem;
    var originalClear = Storage.prototype.clear;

    Storage.prototype.setItem = function(key, value) {
      originalSetItem.call(this, key, value);
      if (this === localStorage) schedulePersist();
    };

    Storage.prototype.removeItem = function(key) {
      originalRemoveItem.call(this, key);
      if (this === localStorage) schedulePersist();
    };

    Storage.prototype.clear = function() {
      originalClear.call(this);
      if (this === localStorage) schedulePersist();
    };
  }

  function loadJson(path, fallback) {
    var raw = xhr('GET', path);
    if (!raw) return fallback;
    try {
      return JSON.parse(raw);
    } catch (e) {
      return fallback;
    }
  }

  hydrateStorage();
  patchStorage();

  window.BTCCRuntime = {
    loadJson: loadJson,
    persistNow: persistSnapshot,
    readState: loadStateSnapshot
  };
})();
