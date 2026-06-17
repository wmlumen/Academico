(function() {
  'use strict';

  var path = window.location.pathname.replace(/\\/g, '/');
  var currentFile = path.split('/').pop();
  var repoIndex = path.lastIndexOf('/BTCC/');
  var repoRelative = repoIndex !== -1 ? path.slice(repoIndex + '/BTCC/'.length) : currentFile;
  var segments = repoRelative.split('/').filter(Boolean);
  var depth = Math.max(0, segments.length - 1);
  var prefix = '';

  if (depth >= 4) prefix = '../../../';
  else if (depth === 3) prefix = '../../';
  else if (depth === 2) prefix = '../';

  function loadJson(file, fallback) {
    return (window.BTCCRuntime && window.BTCCRuntime.loadJson(file, fallback)) || fallback;
  }

  var APP = loadJson('/data/app_config.json', {
    branding: { shortName: 'BTCC' },
    institutionalLinks: []
  });
  var SUBJECTS = loadJson('/data/subjects_catalog.json', []);
  var currentSubject = SUBJECTS.find(function(subject) {
    return repoRelative.indexOf(subject.basePath) === 0;
  }) || null;

  function detectarRol() {
    if (document.body.classList.contains('rol-docente')) return 'docente';
    if (document.body.classList.contains('rol-alumno')) return 'alumno';
    try {
      var login = JSON.parse(localStorage.getItem('alumno_login'));
      if (login && login.num) return 'alumno';
    } catch (e) {}
    try {
      var prefs = JSON.parse(localStorage.getItem('nav_prefs'));
      if (prefs && prefs.rol) return prefs.rol;
    } catch (e) {}
    return 'docente';
  }

  function toHref(relativePath) {
    return prefix + relativePath;
  }

  function getInstitutionalLinks() {
    return (APP.institutionalLinks || []).map(function(link) {
      return {
        name: link.name,
        href: toHref(link.href),
        only: link.only || 'ambos'
      };
    });
  }

  function getPortalesLinks() {
    return SUBJECTS
      .filter(function(subject) { return !!subject.portalHref; })
      .map(function(subject) {
        return {
          name: subject.displayName,
          href: toHref(subject.portalHref),
          only: 'ambos'
        };
      });
  }

  function getSubjectCategories(rol) {
    if (!currentSubject || !currentSubject.sidebar) return [];
    var source = currentSubject.sidebar[rol] || [];
    return source.map(function(category) {
      return {
        name: category.name,
        scope: 'subject',
        links: (category.links || []).map(function(link) {
          return {
            name: link.name,
            href: link.href,
            only: link.only || 'ambos'
          };
        })
      };
    });
  }

  function getCategories(rol) {
    var categories = [];
    categories = categories.concat(getSubjectCategories(rol));
    categories.push({ name: 'Portales', scope: 'root', links: getPortalesLinks() });
    categories.push({
      name: rol === 'docente' ? 'Institucional' : 'Información',
      scope: 'root',
      links: getInstitutionalLinks()
    });
    return categories;
  }

  function initSidebar() {
    if (document.getElementById('nav-sidebar')) return;

    var rol = detectarRol();
    var sidebar = document.createElement('div');
    var handle = document.createElement('button');
    var headerTitle = currentSubject ? currentSubject.displayName : ((APP.branding && APP.branding.shortName) || 'Portal');

    sidebar.id = 'nav-sidebar';
    handle.id = 'nav-handle';
    handle.setAttribute('aria-label', 'Abrir menu de navegacion');
    handle.textContent = '☰';

    var header = document.createElement('div');
    header.className = 'nav-header';
    header.innerHTML = '<h2>' + headerTitle + '</h2><p style="font-size:9px;opacity:0.5">' + currentFile + '</p>';
    sidebar.appendChild(header);

    var rolBar = document.createElement('div');
    rolBar.className = 'nav-rol';
    rolBar.innerHTML = '<span class="rol-badge ' + rol + '">' + (rol === 'docente' ? 'Docente' : 'Alumno') + '</span>';
    sidebar.appendChild(rolBar);

    getCategories(rol).forEach(function(category) {
      if (!category.links || category.links.length === 0) return;

      var title = document.createElement('div');
      title.className = 'nav-cat';
      title.textContent = category.name;
      sidebar.appendChild(title);

      var list = document.createElement('ul');
      list.className = 'nav-links';

      category.links.forEach(function(link) {
        if (link.only === 'docente' && rol !== 'docente') return;
        if (link.only === 'alumno' && rol !== 'alumno') return;

        var item = document.createElement('li');
        var anchor = document.createElement('a');
        var finalHref = category.scope === 'root' ? link.href : link.href;
        var linkFile = finalHref.split('/').pop();

        anchor.href = category.scope === 'root' ? finalHref : link.href;
        if (currentFile === linkFile) anchor.className = 'active';
        anchor.textContent = link.name;

        item.appendChild(anchor);
        list.appendChild(item);
      });

      if (list.childElementCount > 0) sidebar.appendChild(list);
    });

    var footer = document.createElement('div');
    footer.className = 'nav-footer';
    sidebar.appendChild(footer);

    var closeBtn = document.createElement('button');
    closeBtn.id = 'nav-close';
    closeBtn.textContent = '✕';
    closeBtn.setAttribute('aria-label', 'Cerrar menu');
    sidebar.appendChild(closeBtn);

    document.body.insertBefore(sidebar, document.body.firstChild);
    document.body.insertBefore(handle, document.body.firstChild);

    handle.addEventListener('click', function(e) {
      e.stopPropagation();
      sidebar.classList.toggle('open');
    });

    closeBtn.addEventListener('click', function() {
      sidebar.classList.remove('open');
    });

    document.addEventListener('click', function(e) {
      if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && e.target !== handle) {
        sidebar.classList.remove('open');
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') sidebar.classList.remove('open');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSidebar);
  } else {
    initSidebar();
  }
})();
