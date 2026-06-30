import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

import asyncio

class GPSBridge(Node):

	def __init__(self, loop):
		super().__init__("gps_bridge")

		self.loop = loop
		self.latest_gps = {
			"lat": None,
			"lon": None,
			"alt": None
		}

		self.create_subscription(
			NavSatFix,
			"/fix",
			self.gps_callback,
			10
		)

	def gps_callback(self, msg):
		self.latest_gps["lat"] = msg.latitude
		self.latest_gps["lon"] = msg.longitude
		self.latest_gps["alt"] = msg.altitude

		print("GPS:", self.latest_gps)
