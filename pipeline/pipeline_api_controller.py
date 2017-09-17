"""
Script to batch run external API flows
"""

import argparse

import datetime as dt

import os

from pipeline.pipeline_tasks.api_calls import yelp_control as yc
from pipeline.pipeline_tasks.api_calls import civics_control as civc
from pipeline.pipeline_tasks.api_calls import geocode_control as geoc


RUNTIME_ID = str(dt.datetime.now())
SQL_PATH = os.path.join(os.path.dirname(__file__), 'pipeline_tasks')

starttime = dt.datetime.now()

def _str2bool(v):
    """Define a function that converts string to bool used in argparse"""
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_args():
    """ Use argparse to pare command line arguments. """
    parser = argparse.ArgumentParser(description='Control script to run external API tasks')
    parser.add_argument('--db_url',
                        help='Database url string to the db.',
                        type=str,
                        required=True)
    parser.add_argument('--max_attempts',
                        help='Maximum records to attempt. If not specified, the maximum number of records depends on the external API usage limits.',
                        type=int,
                        required=False,
                        metavar='max_records')
    parser.add_argument('--older_than',
                        help='Process only records older than number of days. If not specified, number of days depends on the external API usage limits.',
                        type=int,
                        required=False,
                        metavar='num_days')
    parser.add_argument('--reset_update_time',
                        type=_str2bool,
                        nargs='?',
                        const=True,
                        default=False,
                        help='Reset the API update time on all records')

    api_selection = parser.add_argument_group('API Selection', 'At least one API Selection is required, but all may be selected.')
    api_selection.add_argument('--yelp',
                               type=_str2bool,
                               nargs='?',
                               const=True,
                               default=False,
                               help='Run the Yelp API process')
    api_selection.add_argument('--civics',
                               type=_str2bool,
                               nargs='?',
                               const=True,
                               default=False,
                               help='Run the Google Civics API process')
    api_selection.add_argument('--geocode',
                               type=_str2bool,
                               nargs='?',
                               const=True,
                               default=False,
                               help='Run the Geocode API process',
                               required=False)
    #parser.print_help()
    args = parser.parse_args()
    if not (args.civics or args.geocode or args.yelp):
        print("No APIs selected to run.")
        parser.print_help()
        parser.exit(2);
    return args

def main():
    """Main function to run tasks."""
    print("Starting")
    args = get_args()
        
    if args.reset_update_time:
        reset_update_time = True
        reset_str = ''
    else:
        reset_update_time = False
        reset_str = 'NOT '
    if args.max_attempts:
        max_records = args.max_attempts
    else:
        max_records = -1
    if args.older_than:
        older_than = args.older_than
    else:
        older_than = -1
    print("Should process {} records from those older than {} days. Will {}reset update time".format(max_records, older_than, reset_str))
    if args.yelp:
        yelp_params = yc.get_params(max_records, older_than)
        print("Should process Yelp: max of {} records and older than {} days.".format(yelp_params["max_records"], yelp_params["max_days_to_store"]))
        yelp_ids = yc.get_record_ids(yelp_params)
        if yelp_ids is not None and len(yelp_ids) > 0:
            print("Should update Yelp.")
        else:
            print("Could not get Yelp records to update.")
            if yelp_ids is None:
                print("Internal error.")
            else:
                print("Empty record list.")
            #return
        # TODO: pass the yelp ID list to the script that actually calls the API and updates the data set.
    if args.civics:
        civics_params = civc.get_params(max_records, older_than)
        print("Should process Google Civics: max of {} records and older than {} days.".format(civics_params["max_records"], civics_params["max_days_to_store"]))
        civics_ids = civc.get_record_ids(yelp_params)
        if civics_ids is not None and len(civics_ids) > 0:
            print("Should update Google Civics.")
        else:
            print("Could not get Google Civics records to update.")
            if civics_ids is None:
                print("Internal error.")
            else:
                print("Empty record list.")
            #return
        # TODO: pass the Google Civics ID list to the script that actually calls the API and updates the data set.
    if args.geocode:
        geocode_params = geoc.get_params(max_records, older_than)
        print("Should process Geocode: max of {} records and older than {} days.".format(geocode_params["max_records"], geocode_params["max_days_to_store"]))
        geocode_ids = geoc.get_record_ids(yelp_params)
        if geocode_ids is not None and len(geocode_ids) > 0:
            print("Should update Geocode.")
        else:
            print("Could not get Geocode records to update.")
            if geocode_ids is None:
                print("Internal error.")
            else:
                print("Empty record list.")
            #return
        # TODO: pass the Geocode ID list to the script that actually calls the API and updates the data set.


# LOTS STILL TO DO, primarily need to factor out the APIs so they can
# easily be run separately, and also need to make some schema changes
# to have fields to store the last update time stamp for each type of
# API. Then need to provide a way to select the appropriate records to
# run through the given API.

if __name__ == '__main__':
    main()

