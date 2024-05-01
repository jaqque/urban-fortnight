# two things at once


## one

convert a non-normalized list of song titles, sometimes with artist, sometimes with year to a normalized csv file

* `New Paste 1.txt`
* `to-csv.rb`

## two

compare memory usage between python String class's `replace()` method vs python re module's `sub()` function

* `sample-line` basis for further processing
* `make-file.sh` makes the input files
  * `file.txt` 2.4GiB file; 67,108,864 records
  * `small.txt`  10 records
* `profile.py` and `profile-*.py` implementations using `replace()`
* `profile2.py` and `profile2-*.py` implementations using `sub()`
* `*-fi.py` implementations using memory conserving `fileinput` module
  * pass the input file as an argument
  * provide input on STDIN
  * avoids the `readlines()` problem (see below)
* `*-small.py` uses `small.txt` as input
* `*-gc.py` uses garbage collection in a failed attempt to keep memory usage low
  * using `readlines()` reads a lot into memory. Oops.
* `*-free.py` uses explicit calls to `del` in a failed attempt to keep memory usage low
  * yeah, it's the `readlines()` problem still. 😳
* `compose.yaml` and `Containerfile` image and compose file to run the profiling tests
  * `podman-compose run profile`
  * `docker compose run profile`
