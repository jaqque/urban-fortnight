#!/bin/sh

input=sample-line
output=file.txt
small_file=small.txt
temp=.file.tmp
target_size=2147483648 # 2 * 2 ** ( 3 * 10 ) # eg: 2GiB
lines_in_small=10

# select proper stat(1) arguments
case "$(uname -s)" in
  Darwin) stat_arg='-f%z' ;;
  Linux) stat_arg='-c%s' ;;
  *) printf 'Here%ss a nickel kid. Go buy yourself a real computer.\n' "'"; 
     exit 5 ;;
esac

if ! [ -f "$output" ]; then
  # setup
  cp "$input" "$output"

  # duplicate until 2+G
  while [ "$(stat "$stat_arg" "$output")" -lt "$target_size" ]; do
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
