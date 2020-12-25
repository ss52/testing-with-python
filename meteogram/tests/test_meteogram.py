"""Test use of the meteogram module."""

from meteogram import meteogram


#
# Example starter test
#
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary


#
# Instructor led introductory examples
#
def test_title_case():
    in_str = "test string"
    des = "Test String"

    res = in_str.title()

    assert res == des


#
# Instructor led examples of numerical comparison
#
def test_number():
    pass


#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.ё
    """
    import datetime

    station = "FSD"
    start_date = datetime.datetime(2019, 1, 1, 1)
    end_date = datetime.datetime(2019, 1, 5, 1)

    des = (
        "https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2019&"
        "month1=01&day1=01&hour1=01&minute1=00&year2=2019&month2=01&day2=05&hour2=01&minute2=00&"
        "vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes"
    )

    res_srt = meteogram.build_asos_request_url(station, start_date, end_date)

    assert res_srt == des


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    import datetime

    station = "FSD"
    start_date = datetime.datetime(2019, 11, 11, 16)
    end_date = datetime.datetime(2019, 11, 25, 15)

    des = (
        "https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2019"
        "&month1=11&day1=11&hour1=16&minute1=00&year2=2019&month2=11&day2=25&hour2=15&minute2=00&"
        "vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes"
    )

    res_srt = meteogram.build_asos_request_url(station, start_date, end_date)

    assert res_srt == des


#
# Exercise 1 - Stop Here
#

#
# Exercise 2 - Add calculation tests here
#

#
# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
