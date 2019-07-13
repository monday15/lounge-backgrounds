project('lounge-backgrounds',
  version: '1.0',
  meson_version: '>= 0.41.0'
)

prefix = get_option('prefix')

datadir = join_paths(prefix, get_option('datadir'))
backgrounddir = join_paths(datadir, 'backgrounds', 'lounge')
metadatadir = join_paths(datadir, 'gnome-background-properties')

dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

lounge_timed = configure_file(
  input: 'lounge-timed.xml.in',
  output: 'lounge-timed.xml',
  configuration: dataconf
)

lounge_xml = configure_file(
  input: 'lounge.xml.in',
  output: 'lounge.xml',
  configuration: dataconf
)

backgrounds = [
  'mike-yukhtenko-1471463-unsplash-morning.jpg',
  'mike-yukhtenko-1471463-unsplash-day.jpg',
  'mike-yukhtenko-1479951-unsplash-night.jpg'
]

install_data([lounge_timed] + backgrounds, install_dir: backgrounddir)
install_data([lounge_xml], install_dir: metadatadir)
