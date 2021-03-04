if ! grep -l 'alias adog' ~/.bash_profile >> /dev/null
then
  sh=`basename $SHELL`
  profile=~/.${sh}_profile
  echo >> $profile  # In case the profile doesn't end with a newline
  cat git-aliases.sh >> $profile
  echo Appended git aliases to $profile
fi
