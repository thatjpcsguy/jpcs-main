<VirtualHost *:80>
	ServerAdmin james@cooperstanbury.com
	ServerName cooperstanbury.com
	ServerAlias jpcs.me jamespetercooperstanbury.com

	WSGIDaemonProcess jpcs user=james group=james threads=5
	WSGIScriptAlias / /home/james/jpcs-main/jpcs.wsgi

#	DocumentRoot /var/www/jpcs
	<Directory /home/james/jpcs-main>
#		Options Indexes FollowSymLinks MultiViews
#		AllowOverride None
		WSGIProcessGroup jpcs
		WSGIApplicationGroup %{GLOBAL}
		WSGIScriptReloading On
		Order allow,deny
		Allow from all
	</Directory>
</VirtualHost>
