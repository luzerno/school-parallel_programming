echo "************* thread = 1" > scaleup
echo "************* thread = 1"
java BruteForceDES 1 20 >> scaleup
java BruteForceDES 1 20 >> scaleup
java BruteForceDES 1 20 >> scaleup
java BruteForceDES 1 20 >> scaleup
java BruteForceDES 1 20 >> scaleup

echo "************* thread = 2" >> scaleup
echo "************* thread = 2"
java BruteForceDES 2 21 >> scaleup
java BruteForceDES 2 21 >> scaleup
java BruteForceDES 2 21 >> scaleup
java BruteForceDES 2 21 >> scaleup
java BruteForceDES 2 21 >> scaleup

echo "************* thread = 4" >> scaleup
echo "************* thread = 4"
java BruteForceDES 4 22 >> scaleup
java BruteForceDES 4 22 >> scaleup
java BruteForceDES 4 22 >> scaleup
java BruteForceDES 4 22 >> scaleup
java BruteForceDES 4 22 >> scaleup

echo "************* thread = 8" >> scaleup
echo "************* thread = 8"
java BruteForceDES 8 23 >> scaleup
java BruteForceDES 8 23 >> scaleup
java BruteForceDES 8 23 >> scaleup
java BruteForceDES 8 23 >> scaleup
java BruteForceDES 8 23 >> scaleup

echo "************* thread = 16" >> scaleup
echo "************* thread = 16"
java BruteForceDES 16 24 >> scaleup
java BruteForceDES 16 24 >> scaleup
java BruteForceDES 16 24 >> scaleup
java BruteForceDES 16 24 >> scaleup
java BruteForceDES 16 24 >> scaleup

