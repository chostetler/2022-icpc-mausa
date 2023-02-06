clear
FileName=$(echo "$1" | cut -f 1 -d '.');
datafolder=$(echo "./sampledata/$FileName");
for f in ./sampledata/$FileName/*.in;
do
    echo -n "Test input $(basename $f): "
    answerfile="${f%.*}.ans"
    TIMEFORMAT="(%3R seconds)"
    time $(python $FileName.py < $f > output) > timeuse
    differences=$(diff -y --suppress-common-lines --ignore-trailing-space output $answerfile | wc -l)
    if [ $differences == "0" ]; then
        echo "✅ Passed";
        cat timeuse
    else
        echo "❌ Failed:";
        diff --ignore-trailing-space output $answerfile;
    fi
    rm output
    rm timeuse
    echo ""
done;