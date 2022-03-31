from display import mult_xyzt_plt, display_xyzt, plot_2d
from integrate import integrate_xyzt
from parse_csv import csv_to_list
from pre_precess import sub_avg_all

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

    (x, y, z, t) = tlsts 
    tlsts_modded = sub_avg_all([x, y, z], 8)
    print("-------")
    tlsts_modded.append(t)
    tlsts = tuple(tlsts_modded)
    (x, y, z, t) = tlsts 
    print("-------")
    print(tlsts)

    # plot_2d(x,y,z ,t)


    mult_xyzt_plt(
        [tlsts,
         integrate_xyzt(
             integrate_xyzt(tlsts, mode="trap"),
             mode="trap")])

        #  integrate_xyzt(integrate_xyzt(tlsts, c_tuple=(0,0,0), mode="trap"), c_tuple=(0, 0, 0),mode="trap")])
    # mult_xyzt_plt([integrate_xyzt(integrate_xyzt(tlsts))])