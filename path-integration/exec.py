from display import mult_xyzt_plt, display_xyzt
from integrate import integrate_xyzt
from parse_csv import csv_to_list

if __name__ == '__main__':
    # tlsts = csv_to_list("path-raw-csv/o.csv")
    tlsts = csv_to_list("o.csv")
    # tlsts = integrate_xyzt(tlsts)
    # print(tlsts())
    # tlsts = integrate_xyzt(integrate_xyzt(tlsts))

    # display_xyzt(tlsts)
    mult_xyzt_plt([tlsts, integrate_xyzt(integrate_xyzt(tlsts))])
    # mult_xyzt_plt([integrate_xyzt(integrate_xyzt(tlsts))])