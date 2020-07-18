for ((test=1;test<10; test++))
do
	echo Test $test
	vertices=$(python3 -c "import random; print(random.randint(3,100))")
	cd ../code
	python3 -c "import regular_polygon; print(regular_polygon.regular_polygon(100, $(expr $test + 3)))" > ../test/out
	cd ../test
	python3 -c "import regular_polygon; print(regular_polygon.regular_polygon(100, $(expr $test + 3)))" > ans
	diff out ans
	if [[ $? -ne 0 ]]
	then 
	   echo Wrong answer
           echo Wrong with input $vertices 
	   break
	else
	   echo "Pass!"
	fi
done
