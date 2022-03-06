for x in {5..40}
do
    for y in {5..40}
    do
        python3 digits.py $x $y > /dev/null
        echo "X = "$x" Y = "$y
        #python3 knn.py features.txt
        output=$(python3 knn.py features.txt)
        echo "$output" | grep "accuracy"
    done
done
