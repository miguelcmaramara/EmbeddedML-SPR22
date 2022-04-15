from display import mult_xyzt_plt, display_xyzt, plot_2d
from integrate import integrate_xyzt
from parse_csv import csv_to_list
from pre_precess import sub_avg_all, sub_avg, apply_to_all, correct_units
from kalman import apply_kalman

if __name__ == '__main__':
    # tlsts = csv_to_list("path-raw-csv/o.csv")
    # tlsts = csv_to_list("o.csv")[1]
    # tlsts = integrate_xyzt(tlsts)
    # print(tlsts())
    # tlsts = integrate_xyzt(integrate_xyzt(tlsts))

    # mult_xyzt_plt(
    #     [tlsts,
    #      integrate_xyzt(integrate_xyzt(tlsts, c_tuple=(-.83, .5, 0), mode="trap"), c_tuple=(0, 0, 0),mode="trap")])

    # print(len(csv_to_list("path-integration/path-sync-csv/data_collection1.csv")))

    # tlsts = csv_to_list("path-integration/path-sync-csv/data_collection2.csv")[12]
    tlsts = csv_to_list("path-integration/path-sync-csv/meeting-with-purwar.csv")[6]
    print(tlsts)

    # Kalman's filter
    # 

    (x, y, z, t) = tlsts 

    # -----
    # Pre-processing
    # -----

    # Correcting force units
    tlsts_modded = apply_to_all(
        lambda lst: correct_units(lst, 10),
        [x,y,z]
    )
    # Correcting time units
    t = correct_units(t, .001)
    tlsts_modded = sub_avg_all([x, y, z], 8)
    # tlsts_modded = apply_to_all(lambda a:sub_avg(a, 8), [x,y,z])
    tlsts_modded.append(t)
    tlsts = tuple(tlsts_modded)
    (x, y, z, t) = tlsts 

    xkal = apply_kalman(t, x)
    ykal = apply_kalman(t, y)
    zkal = apply_kalman(t, z)
    tlsts = (xkal, ykal, zkal, t)


    (x, y, z, t) = tlsts 
    print(tlsts)

    plot_2d(x,y,z ,t)
    # plot_2d(y,ykal,z ,t)


    mult_xyzt_plt(
        [tlsts,
         integrate_xyzt(
             integrate_xyzt(tlsts, mode="trap"),
             mode="trap")])

        #  integrate_xyzt(integrate_xyzt(tlsts, c_tuple=(0,0,0), mode="trap"), c_tuple=(0, 0, 0),mode="trap")])
    # mult_xyzt_plt([integrate_xyzt(integrate_xyzt(tlsts))])