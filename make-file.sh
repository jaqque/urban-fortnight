#!/bin/sh

input=sample-line
output=file.txt
small_file=small.txt
temp=.file.tmp
target_size=2147483648 # 2 * 2 ** ( 3 * 10 ) # eg: 2GiB
lines_in_small=10

if ! [ -f "$output" ]; then
  # setup
  cp "$input" "$output"

  # duplicate until 2+G
  while [ "$(stat -f%z "$output")" -lt "$target_size" ]; do
    cat "$output" "$output" > "$temp"
    mv "$temp" "$output"
    printf .
  done
  tput dl1 # clear to beginning of line
  printf '\r' # return cursoe to beginning of line
fi

if ! [ -f "$small_file" ]; then
  # make smaller sample
  head -n "$lines_in_small" "$output" > "$small_file"
fi
