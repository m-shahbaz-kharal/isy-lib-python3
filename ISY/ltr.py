# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 01:49:02 2018

@author: MShah
"""

EVENT_CTRL_ACTION  = {
    "_0" : { },

    "_1" : {
	'0': "Event Status",
	'1': "Get Status",
	'2': "Key Change",
	'3': "Info String",
	'4': "IR Learn Mode",
	'5': "Schedule",
	'6': "Var Stat",
	'7': "Var Init",
	'8': "Key",
	},

    # Driver Specific Events
    "_2" : {},

    # Node Changed/Updated
    '_3': {
	'NN': 'Node Renamed',
	'NR': 'Node Removed',
	'ND': 'Node Added',
	'MV': 'Node Moved (into a scene)',
	'CL': 'Link Changed (in a scene)',
	'RG': 'Removed From Group (scene)',
	'EN': 'Enabled',
	'PC': 'Parent Changed',
	'PI': 'Power Info Changed',
	'DI': 'Device ID Changed',
	'DP': 'Device Property Changed',
	'GN': 'Group Renamed',
	'GR': 'Group Removed',
	'GD': 'Group Added',
	'FN': 'Folder Renamed',
	'FR': 'Folder Removed',
	'FD': 'Folder Added',
	'NE': 'Node Error (Comm. Errors)',
	'CE': 'Clear Node Error (Comm. Errors Cleared)',
	'SN': 'Discovering Nodes (Linking)',
	'SC': 'Node Discovery Complete',
	'WR': 'Network Renamed',
	'WH': 'Pending Device Operation',
	'WD': 'Programming Device',
	'RV': 'Node Revised (UPB)',
	},

    # System Configuration Updated
    '_4': {
	'0': 'Time Changed',
	'1': 'Time Configuration Changed',
	'2': 'NTP Settings Updated',
	'3': 'Notifications Settings Updated',
	'4': 'NTP Communications Error',
	'5': 'Batch Mode Updated',
	'6': 'Battery Mode Programming Updated',
	},

    # System Status Updated
    '_5': {
	'0': 'Not Busy',
	'1': 'Busy',
	'2': 'Idle',
	'3': 'Safe Mode',
	},

    # Internet Access Status
    '_6': {
	'0': 'Disabled',
	'1': 'Enabled',
	'2': 'Failed',
	},

    # Progress Report
    '_7': {
	'1': 'Update',
	'2.1': 'Device Adder Info (UPB Only)',
	'2.2': 'Device Adder Warn (UPB Only)',
	'2.3': 'Device Adder Error (UPB Only)',
	},

    # Security System Event
    '_8': {
	'0': 'Disconnected',
	'1': 'Connected',
	'DA': 'Disarmed',
	'AW': 'Armed Away',
	'AS': 'Armed Stay',
	'ASI': 'Armed Stay Instant',
	'AN': 'Armed Night',
	'ANI': 'Armed Night Instant',
	'AV': 'Armed Vacation',
	},

    # System Alert Event
    "_9" : {},

    # Electricity / OpenADR and Flex Your Power Events
    '_10': {
	'1': 'Open ADR Error',
	'2': 'Open ADR Status Update',
	'5': 'Flex Your Power Error',
	'6': 'Flex Your Power Status Updated',
	'8': 'OpenADR Registration Status',
	'9': 'OpenADR Report Status',
	'10': 'OpenADR Opt Status',
	},


    # Climate Events
    '_11': {
	'0': 'Error',
	'1': 'Temperature',
	'2': 'Temperature High',
	'3': 'Temperature Low',
	'4': 'Feels Like',
	'5': 'Temperature Rate',
	'6': 'Humidity',
	'7': 'Humidity Rate',
	'8': 'Pressure',
	'9': 'Pressure Rate',
	'10': 'Dew Point',
	'11': 'Wind Speed',
	'12': 'Average Wind Speed',
	'13': 'Wind Direction',
	'14': 'Average Wind Direction',
	'15': 'Gust Wind Speed',
	'16': 'Gust Wind Direction',
	'17': 'Rain Today',
	'18': 'Ambient Light',
	'19': 'Light Rate',
	'20': 'Rain Rate',
	'21': 'Rain Rate Max',
	'22': 'Evapotranspiration',
	'23': 'Irrigation Requirement',
	'24': 'Water Deficit Yesterday',
	'25': 'Elevation',
	'26': 'Coverage',
	'27': 'Intensity',
	'28': 'Weather Condition',
	'29': 'Cloud Condition',
	'30': "Tomorrow's Forecast: Average Temperature",
	'31': "Tomorrow's Forecast: High Temperature",
	'32': "Tomorrow's Forecast: Low Temperature",
	'33': "Tomorrow's Forecast: Humidity",
	'34': "Tomorrow's Forecast: Wind Speed",
	'35': "Tomorrow's Forecast: Gust Speed",
	'36': "Tomorrow's Forecast: Rain",
	'37': "Tomorrow's Forecast: Snow",
	'38': "Tomorrow's Forecast: Coverage",
	'39': "Tomorrow's Forecast: Intensity",
	'40': "Tomorrow's Forecast: Weather Condition",
	'41': "Tomorrow's Forecast: Cloud Condition",
	'42': '24 Hour Forecast: Average Temperature',
	'43': '24 Hour Forecast: High Temperature',
	'44': '24 Hour Forecast: Low Temperature',
	'45': '24 Hour Forecast: Humidity',
	'46': '24 Hour Forecast: Rain',
	'47': '24 Hour Forecast: Snow',
	'48': '24 Hour Forecast: Coverage',
	'49': '24 Hour Forecast: Intensity',
	'50': '24 Hour Forecast: Weather Condition',
	'51': '24 Hour Forecast: Cloud Condition',
	'100': 'Last Updated Timestamp',
	},

    # ISY SEP EVENTS
    '_12': {
	'1': 'Network Status Changed',
	'2': 'Time Status Changed',
	'3': 'New Message',
	'4': 'Message Stopped',
	'5': 'New Price',
	'6': 'Price Stopped',
	'7': 'New DR Event',
	'8': 'DR Event Stopped',
	'9': 'Metering Event',
	'10': 'Metering Format Event',
	'31': 'Scheduled Message',
	'51': 'Scheduled Price',
	'71': 'Scheduled DR Event',
	'110': 'Fast Poll Mode',
	'111': 'Normal Poll Mode',
	},

    # External Energy Monitoring Events
    '_13': {
	'1': 'Number of Channels',
	'2': 'Channel Report',
	'3': 'Zigbee Status',
	'7': 'Raw Packet',
	},

    # UPB Linker Events
    '_14': {
	'1': 'Device Status',
	'2': 'Pending Stop Find',
	'3': 'Pending Cancel Device Adder',
	},

    # UPB Dev State
    '_15': {},

    # UPB Device Status Events
    '_16': {
	'1': 'Device Signal Report',
	'2': 'Device Signal Report Removed',
	},

    # Gas Meter Events
    '_17': {
	'1': 'Status',
	'2': 'Error',
	},

    # Zigbee Events
    '_18': {
	'1': 'Status',
	},

    # ELK
    "_19" : {},

    # Device Linker Events
    '_20': {
	'1': 'Status',
	'2': 'Cleared',
	},

    # Z-Wave
    "_21" : {},

    # Billing Events
    '_22': {
	'1': 'Cost/Usage Changed Event',
	},

    # Portal Events
    '_23': {
	'1': 'Status',
	},

}