from display import mult_xyzt_plt, display_xyzt, plot_2d
from integrate import integrate_xyzt
from parse_csv import csv_to_list
from pre_precess import sub_avg_all, sub_avg, all_to_all, apply_to_all, correct_units, low_pass_filter, averaging_filter, append_numbers
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
    # tlsts = csv_to_list("path-integration/path-sync-csv/meeting-with-purwar.csv")[6]
    tlsts = csv_to_list("path-integration/path-sync-csv/data_collection3.csv")[3]
    print(tlsts)

    (x, y, z, t) = tlsts 

    # -----
    # Pre-processing
    # -----

    # Correcting force units
    tlsts_modded = sub_avg_all([x, y, z], 8)
    (x, y, z) = tlsts_modded

    # x = apply_kalman(t, x)
    # y = apply_kalman(t, y)
    # z = apply_kalman(t, z)

    tlsts_modded = all_to_all(
        [
            lambda lst: append_numbers(lst, 10, num_to_append=0),
            lambda lst: correct_units(lst, 10),
            lambda lst: averaging_filter(lst, 30, trailing=True),
            lambda lst: low_pass_filter(lst, .1, center_only=True),
            # lambda lst: low_pass_filter(lst, .05, center_only=False)
        ],
        [x,y,z]
    )
    # tlsts_modded = apply_to_all(
    #     lambda lst: correct_units(lst, 10),
    #     [x,y,z]
    # )
    # Correcting time array
    t = correct_units(t, .001)
    t = append_numbers(t, 10, stretch=True)
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

    (xvel, yvel, zvel, tvel) = integrate_xyzt(tlsts, mode="trap", vel_fact=True)
    # (xvel, yvel, zvel, tvel) = integrate_xyzt(tlsts, mode="trap")
    plot_2d(xvel,yvel,zvel ,tvel)

    # plot_2d(y,ykal,z ,t)


    mult_xyzt_plt(
        [tlsts,
         integrate_xyzt(
             integrate_xyzt(tlsts, mode="trap", vel_fact=True),
            #  integrate_xyzt(tlsts, mode="trap"),
             mode="trap")])

        #  integrate_xyzt(integrate_xyzt(tlsts, c_tuple=(0,0,0), mode="trap"), c_tuple=(0, 0, 0),mode="trap")])
    # mult_xyzt_plt([integrate_xyzt(integrate_xyzt(tlsts))])