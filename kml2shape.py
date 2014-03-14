import xml.etree.ElementTree as ET
import csv
import StringIO

def main():
	with open('shapes.txt', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow(["shape_id","shape_pt_sequence","shape_dist_traveled","shape_pt_lat","shape_pt_lon"])
		prefix = 'data/GCT_Route'
		routes = {"101": "","102": "","103": "","103A": "","10B": "","20": "","30": "","35": "","40": "","410": "","412": "","418": "","10A": ""}
		for route in routes.keys():
			fn = prefix + route
			tree = ET.parse(fn + '.kml')
			root = tree.getroot()
			# scsv = ''
			routes[route] = get_coordinates(root).split()
			reader = csv.reader(routes[route], delimiter=',')
			# row_count = sum(1 for row in reader)
			count = sum(1 for word in routes[route])
			print count
			
			i = 0
			for row in reader:
				# if i==0:
				# 	
				spamwriter.writerow([route + 'A', str(i), '' , row[1], row[0]])
				spamwriter.writerow([route + 'B', str(count - i), '' , row[1], row[0]])
				i += 1
			# j = 0
			# for row in reversed(list(reader)):
			# 	spamwriter.writerow([route + 'B', str(j), '' , row[1], row[0]])
			# 	# print route + 'B,' + str(j) + ',,' + row[1] + ',' +  row[0]
			# 	j += 1
			# print j

def get_coordinates(root):
	coords = ""
	for coordinates in root.iter('{http://www.opengis.net/kml/2.2}coordinates'):
		# print coordinates.text
		coords += coordinates.text
	return coords
if __name__ == '__main__':
	main()