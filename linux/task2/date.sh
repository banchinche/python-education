#!/bin/bash
touch $HOME/date.txt | echo `date +"%D - %H:%M:%S"` >> $HOME/date.txt
