import sys, time
import sevseg

second_left = 30

try:
    while True:
        print('\n'*60)

        hours = str(second_left // 3600)

        minutes = str((second_left % 3600) // 60)

        seconds = str(second_left % 60)

        h_digits = sevseg.getSevSegStr(hours, 2)

        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = sevseg.getSevSegStr(minutes, 2)

        m_top_row , m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = sevseg.getSevSegStr(seconds, 2)

        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        print(h_top_row  + '  ' + h_middle_row + '  ' + h_bottom_row)
        print(m_top_row  + '  ' + m_middle_row + '  ' + m_bottom_row)
        print(s_top_row  + '  ' + s_middle_row + '  ' + s_bottom_row)

        if second_left == 0:
            print()
            print('    * * * * BOOM * * * *')
            break
        print()
        print("Press Ctrl-C to quit")

        time.sleep(1)

        second_left -= 1
except KeyboardInterrupt:
    print('Countdown, by Sam kanja')
    sys.exit()





                     