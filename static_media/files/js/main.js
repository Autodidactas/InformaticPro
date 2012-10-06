// Google Plus
window.___gcfg = {lang: 'es-419'};

	(function() {
		var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
		po.src = 'https://apis.google.com/js/plusone.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
	})();
	
// Facebook "Me Gusta"
(function(d, s, id) {
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) return;
	js = d.createElement(s); js.id = id;
	js.src = "http://connect.facebook.net/es_LA/all.js#xfbml=1";
	fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Contador
$(function () {
	var austDay = new Date();
	austDay = new Date(austDay.getFullYear(), 12 - 2, - 23);
	$('#cuenta-regresiva').countdown({until: austDay, serverSync: ahead5Mins, layout: '<li>{dn}<span>Días</span></li><li>{hn}<span>Horas</span></li><li>{mn}<span>Minutos</span></li><li>{sn}<span>Segundos</span></li>'});
});

// Sincronización del servidor (simulados 5 minutos antes)
function ahead5Mins() { 
    var server = new Date(); 
    server.setMinutes(server.getMinutes() + 120); 
    return server; 
}
// DISQUS
var disqus_shortname = 'felixricarb';
(function() {
	var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
	dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
	(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
})();