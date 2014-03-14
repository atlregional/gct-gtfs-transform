gct-gtfs-transform
==================

Scripts to add kml shape information to GCT GTFS

## Usage

1. Make sure updated kml files are located in `/data` and are generically named `GCT_Route{route_name}.kml`.
2. Run `python kml2shape.py`.
3. `shapes.txt` will be overwritten with new data.
4. Run `java -jar -Xmx4G -server /path/to/onebusaway-gtfs-transformer-cli-1.3.3.jar --transform=match.json /path/to/gtfs.zip /path/to/gtfs_out.zip`.
5. Update `shape_id` field in `trips.txt` to account for differing trip directions.