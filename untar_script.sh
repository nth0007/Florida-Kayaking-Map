for f in *.tar.gz
do
	echo "Untarring $f"
	tar -zxvf $f
done

rm *_B1.TIF *_B7.TIF *_B8.TIF *_B9.TIF *_B10.TIF *_B11.TIF *_BQA.TIF
