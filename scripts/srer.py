import click
import urllib.request
import utils

@click.group()
def main():
    pass

@main.command()
def raingages():
    url = "https://cals.arizona.edu/SRER/precip/rainstautm.txt"
    click.echo("Downloading raingage utm coords.")
    click.echo("Download source: {}".format(url))    
    with urllib.request.urlopen(url) as f:
        line_count = 0
        lines = f.readlines()
        for l in lines:
            line = l.decode('utf-8').strip()
            if len(line) > 0:
                if line_count > 4 and line_count < 80:
                    station_code = line[0:12].strip()
                    current_station_name = line[12:33].strip()
                    xcoord = line[33:51].strip()
                    ycoord = line[51:].strip()
                    latitude, longitude = utils.utm_to_latlon(12, float(xcoord), float(ycoord))
                    # print([
                    #     line_count,
                    #     station_code,
                    #     current_station_name,
                    #     xcoord,
                    #     ycoord,
                    #     latitude,
                    #     longitude
                    # ])                        
                line_count += 1

    f.close()

    click.echo("Done!")

def precip():
    url = ""
    click.echo("Downloading precipitation data.")
    click.echo("Download source: {}".format(url)) 

if __name__ == "__main__":    
    precip()
    # main()