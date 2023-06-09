(function ()
{
    if (!(window.TV && window.TV.Core))
    {
        if (!window.TVCoreLoad)
        {
            window.TVAssets = {
                stours: 'stours.min.js',
                slider: 'slider.min.js',
                minprice: 'minprice.min.js',
                geo: 'geo.min.js',
                feed: 'feed.min.js',
                country: 'country.min.js',
                core2: 'core2.min.js',
                core: 'core.min.js',
                calendar: 'calendar.min.js'
            };

            var tourvisorfindGET = function (name, search)
            {
                var result = false,
                    tmp = [];
                search = search !== undefined ? search : location.search;

                search
                    .substr(1)
                    .split('&')
                    .forEach(function (item)
                    {
                        tmp = item.split('=');
                        if (tmp[0] === name) result = decodeURIComponent(tmp[1]);
                    });
                return result;
            };

            window.TVCoreLoad = true;

            var js = document.createElement('script'),
                head = document.head || document.getElementsByTagName('head')[0],
                root = '//tourvisor.ru/module/v5.0.13/',
                version;

            switch (true) {
                case tourvisorfindGET('tvtest') === 'ok':
                    version = '?v=' + new Date().getTime();
                    root = root.replace(/\/v.+\//, '/modules-test/');
                    for(var k in window.TVAssets) {
                        window.TVAssets[k] = window.TVAssets[k].replace(/\.([\S]){20}/, '.min');
                    }
                    break;
                case tourvisorfindGET('tvbeta') === 'ok':
                    version = '?v=' + new Date().getTime();
                    root = root.replace(/\/v.+\//, '/beta-test/');
                    for(var k in window.TVAssets) {
                        window.TVAssets[k] = window.TVAssets[k].replace(/\.([\S]){20}/, '.min');
                    }
                    break;
                default:
                    version = '?v=' + 1675853284749;
                    var srcFolder = tourvisorfindGET('tvfolder');
                    if(srcFolder !== false){
                        root = root.replace(/\/v.+\//, '/' + srcFolder + '/');
                        for(var k in window.TVAssets) {
                            window.TVAssets[k] = window.TVAssets[k].replace(/\.([\S]){20}/, '.min');
                        }
                    }
                    break;
            }

            js.setAttribute('type', 'text/javascript');
            js.setAttribute('charset', 'utf-8');
            js.setAttribute('src', root + window.TVAssets.core + version);
            head.insertBefore(js, head.firstChild);

            if (js.onload === null)
            {
                js.onload = function ()
                {
                    TV.loadModules();
                };
            }
            else
            {
                js.onreadystatechange = function ()
                {
                    if (this.readyState == 'complete')
                    {
                        TV.loadModules();
                    }
                };
            }
        }
    }
    else
    {
        TV.loadModules();
    }
})();
