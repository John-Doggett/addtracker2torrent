import sys
import bencode

# Check if the file name of the torrent file is given as a command line argument
if len(sys.argv) < 2:
    print('Usage: python add_trackers.py <torrent_file>')
    sys.exit(1)

# Get the file name of the torrent file from the command line arguments
torrent_file = sys.argv[1]

# Open the torrent file
try:
    with open(torrent_file, 'rb') as f:
        torrent_data = f.read()
except FileNotFoundError:
    print(f'Error: file {torrent_file} not found')
    sys.exit(1)

# Decode the torrent data using bencode
torrent_dict = bencode.decode(torrent_data)

# Add the new trackers to the list of existing trackers
new_trackers = [
    'http://tracker.opentrackr.org:1337/announce',
    'http://tracker.openbittorrent.com:80/announce',
    'http://tracker1.bt.moack.co.kr:80/announce',
    'http://tracker.gbitt.info:80/announce',
    'http://open.acgnxtracker.com:80/announce',
    'http://tracker.lelux.fi:80/announce',
    'http://tracker2.dler.org:80/announce',
    'http://tracker.dler.org:6969/announce',
    'http://incine.ru:6969/announce',
    'http://tracker.renfei.net:8080/announce',
    'http://tracker.qu.ax:6969/announce',
    'http://tracker.mywaifu.best:6969/announce',
    'http://tracker.edkj.club:6969/announce',
    'http://parag.rs:6969/announce',
    'http://montreal.nyap2p.com:8080/announce',
    'http://fosstorrents.com:6969/announce',
    'http://dht.dhtclub.com:666/announce',
    'http://bt.okmp3.ru:2710/announce',
    'http://wepzone.net:6969/announce',
    'http://tracker.bt4g.com:2095/announce',
    'http://bt1.letpo.com:80/announce',
    'http://1337.abcvg.info:80/announce',
    'http://uraniumhexafluori.de:1919/announce',
    'http://tracker1.itzmx.com:8080/announce',
    'http://t.acg.rip:6699/announce',
    'http://bt.endpot.com:80/announce'
]

if 'announce-list' not in torrent_dict:
    torrent_dict['announce-list'] = []

# Append the new trackers to the existing tracker list
for tracker in new_trackers:
    if [tracker] not in torrent_dict['announce-list']:
        torrent_dict['announce-list'].append([tracker])

# Encode the updated torrent dictionary into bencoded format
updated_torrent_data = bencode.encode(torrent_dict)

# Write the updated torrent data to the torrent file
with open(torrent_file, 'wb') as f:
    f.write(updated_torrent_data)
