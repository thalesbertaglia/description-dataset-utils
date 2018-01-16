'''Useful functions for processing the movie description dataset.'''

# Author: Thales Bertaglia <thalesbertaglia@gmail.com>

import re


def string_to_seconds(time_string):
    '''Converts a time string in format '00.00.30.057' to seconds'''
    h, m, s, ms = time_string.split('.')
    return ((int(h) * 3600) + (int(m) * 60) + int(s) + (int(ms) / 1000))


def extract_by_id(in_file, out_path, write_log=False):
    '''Extracts descriptions by movie id and saves each one in a different file according to their id.'''
    with open(in_file) as f:
        # Used to decide whether to create a new file
        ids = dict()
        # Movie title by id
        if write_log: log = open('id-titles.txt','w')
        out = None
        for line in f:
            film_id = line.split('_')[0]
            if film_id not in ids:
                ids[film_id] = 0
                if write_log: log.write(film_id + '\t' + re.split(r'\d+',line)[1].replace('_',' ').strip()+'\n')
                if out:
                    out.flush()
                    out.close()
                out = open(out_path+film_id + '.txt','w')
            out.write(line)


def get_total_duration(in_file):
    '''Calculates the total duration of descriptions/subtitles contained in file :in_file:'''
    duration = 0
    with open(in_file) as f:
        for line in f:
            # Gets start and end time of given description
            start, end = line.split('\t')[0].split('_')[-1].split('-')
            duration += string_to_seconds(end) - string_to_seconds(start)
    return duration


def filter_by_duration(in_file, threshold):
    '''Returns a list of clips with total duration <= the given threshold (in seconds).'''
    desc = []
    with open(in_file) as f:
        for line in f:
            # Gets start and end time of given description
            start, end = line.split('\t')[0].split('_')[-1].split('-')
            duration = string_to_seconds(end) - string_to_seconds(start)
            if duration <= threshold:
                desc.append(line.split('\t')[0].strip())
    return desc
