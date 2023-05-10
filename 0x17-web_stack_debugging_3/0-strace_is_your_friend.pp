# Apache returns 500; use this script to fix typo in config

exec { 'fix-wordpress':
  command => "/bin/sed -i /var/www/html/wp-settings.php \
  -e 's/class-wp-locale.phpp/class-wp-locale.php/'"
}
