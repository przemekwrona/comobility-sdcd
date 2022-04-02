import os
from experiments import delay_detector
from experiments import delay_detector_by_hour
from python.plot import delay_detector_plot

RESULTS_DIRECTORY = 'results/delay'
RESULTS_BY_HOUR_DIRECTORY = 'results/delay_by_hour'

ALL_DATA = ['2021-12-11', '2021-12-12', '2021-12-13', '2021-12-14', '2021-12-15', '2021-12-16', '2021-12-17',
            '2021-12-18', '2021-12-19', '2021-12-20', '2021-12-21']
MONDAY_FRIDAY_DATA = ['2021-12-13', '2021-12-14', '2021-12-15', '2021-12-16', '2021-12-17',
                      '2021-12-20', '2021-12-21']

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if not os.path.exists(RESULTS_DIRECTORY):
        os.makedirs(RESULTS_DIRECTORY)

    if not os.path.exists(RESULTS_BY_HOUR_DIRECTORY):
        os.makedirs(RESULTS_BY_HOUR_DIRECTORY)

    # delay_detector.run(results_file_name='results/detected_changes.csv',
    #                    results_path='results/delay',
    #                    scope=ALL_DATA,
    #                    options={'detector_key_type': 'TWO_STOPS'})
    #
    delay_detector_plot.generate_results('results/detected_changes.csv', 'results/delay',
                                         '2021-12-18', '2021-12-21', '2021-12-20')

    # delay_detector_plot.generate_latex(results_path='results/detected_changes.csv', target_path='results/delay',
    #                                    date_from='2021-12-18', date_to='2021-12-22', algorithm_type='ADWIN',
    #                                    detector='DELAY_DETECTOR')

    # delay_detector_plot.generate_latex(results_path='results/detected_changes.csv', target_path='results/delay',
    #                                    date_from='2021-12-18', date_to='2021-12-22', algorithm_type='ADWIN',
    #                                    detector='DELTA_DETECTOR')

    delay_detector_plot.generate_latex(results_path='results/detected_changes.csv', target_path='results/delay',
                                       date_from='2021-12-18', date_to='2021-12-22', algorithm_type='KSWIN',
                                       detector='DELAY_DETECTOR')
    #
    # delay_detector_plot.generate_latex(results_path='results/detected_changes.csv', target_path='results/delay',
    #                                    date_from='2021-12-18', date_to='2021-12-22', algorithm_type='KSWIN',
    #                                    detector='DELTA_DETECTOR')

    # delay_detector_plot.generate_latex(results_path='results/detected_changes.csv', target_path='results/delay',
    #                                    date_from='2021-12-18', date_to='2021-12-22', algorithm_type='HDDMA',
    #                                    detector='DELAY_DETECTOR')
    #
    # delay_detector_plot.generate_latex(results_path='results/detected_changes.csv', target_path='results/delay',
    #                                    date_from='2021-12-18', date_to='2021-12-22', algorithm_type='HDDMA',
    #                                    detector='DELTA_DETECTOR')

    # delay_detector.run(results_file_name='results/detected_changes_hour_detector.csv',
    #                    results_path='results/delay_by_hour',
    #                    scope=ALL_DATA,
    #                    options={'detector_key_type': 'TWO_STOPS_AND_HOUR'})

    # delay_detector_plot.generate_latex('results/detected_changes.csv', 'results/delay', '2021-12-11', '2021-12-21', 'ADWIN', 'DELTA_DETECTOR')

    # delay_detector_plot.generate_results('results/detected_changes_hour_detector.csv', 'results/delay_by_hour',
    #                                      '2021-12-18', '2021-12-21', '2021-12-21')
