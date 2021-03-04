cd .git/objects/pack
for i in pack-*.pack
do
  mv $i ../..
  git unpack-objects < ../../$i
  if [[ $? -ne 0 ]]
  then
    echo $@
    exit $?
  fi
  rm -f ../../$i
  rm -f pack-*.idx
done
