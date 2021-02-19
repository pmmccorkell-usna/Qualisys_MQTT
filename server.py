#
# IPs for different MQTT server Pis.
# Only uncomment one, depending on which server you desire.
#
server="127.0.0.1"	# loopback
# server="172.30.35.102"	# Pat's desk
# server="172.30.38.181"	# SURF nonet
# server="192.168.5.4"      # SURFnet


# pick a unique clientname to prevent collisions with other clients
# Only uncomment one, depending on which server you desire.
# clientname="mydesk"			# Pat's desk
clientname="surfpi_sub"		# SURF
# clientname="reddwarf"		# submarine

# filename='/Users/Levi DeVries/Downloads/mqtt_1.log'
default_directory='/mnt/c/Python/Qualisys_MQTT/log/'


topiclist=[
	'timestamp',
    'STARBOARD ROTOR',
    'PORT ROTOR',
    'W2P2',
    'KITE',
    'bodyD',
	'head',
    'L-frame'
]


#DEBUGGING=0
DEBUGGING=1