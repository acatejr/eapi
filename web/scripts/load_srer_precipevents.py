# from apps.wgew.models import PrecipEvent, Raingage
from apps.srer.models import PrecipEvent, Raingage

def precip_values(values):
    output = []

    for k, v in enumerate(values):
        if v in ['-9999', '']:
            output.append(None)
        else:
            output.append(float(int(v) / 100.00))
    return output

def run(*args):
    if len(PrecipEvent.objects.all()) > 0:
        PrecipEvent.objects.all().delete()

    print("Loading SRER precip events.")
    with open('./data/srer_precip.csv') as f:
        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')
                station = values[0]
                year = values[1]
                precip_vals = precip_values(values[2:])
                rg = Raingage.objects.filter(station_code=station).first()
                if rg == None:
                    rg = Raingage.objects.filter(current_station_name=station).first()
                for k, v in enumerate(precip_vals):
                    event = PrecipEvent(
                        rain_gage = rg,
                        year = year,
                        month = k,
                        precip = v
                    )

                    event.save()
    f.close()

    print("Done!")

