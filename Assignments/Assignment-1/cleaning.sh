find data/*/NOTES
rm data/Frank_Richard/NOTES
rm data/jamesm/NOTES
mkdir cleaned_data
mv data cleaned_data
cd cleaned_data
cd data
for file in */*; do mv $file $file.txt;done


