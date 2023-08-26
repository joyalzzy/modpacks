while read p; do
  echo "adding $p"
  packwiz modrinth add -y $p 
done < $1

