from apps.wgew.models import PrecipEvent, Raingage

def run(*args):
    if len(PrecipEvent.objects.all()) > 0:
        PrecipEvent.objects.all().delete()
        
    with open('./data/wgew_precip_events.csv') as f:
        events = []
        rg = None
        current_raingage_id = None

        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')

                gage = values[0]
                dt = values[1].split('/')
                tm = values[2]
                duration = values[3]
                depth = values[4]
                time_est = values[5]

                if len(dt[0]) == 1:
                    mo = '0{}'.format(dt[0])
                else:
                    mo = dt[0]

                if len(dt[1]) == 1:
                    dy = '0{}'.format(dt[1])
                else:
                    dy = dt[1]

                if len(dt[2]) == 1:
                    yr = '0{}'.format(dt[2])
                else:
                    yr = dt[2]
                
                dt = '{}-{}-{}'.format(yr, mo, dy)

                # Raingage 6 is not in the db, it raises exception.
                try:
                    if (current_raingage_id != gage):
                        rg = Raingage.objects.filter(gage_id=gage, watershed_id=63)[0]
                        current_raingage_id = gage

                    pe = PrecipEvent(
                        rain_gage = rg,
                        event_date = dt,
                        event_time = tm,
                        duration = duration,
                        depth = depth,
                        time_est = time_est
                    )
                    pe.save()
                except Exception:
                    pass
    f.close()
