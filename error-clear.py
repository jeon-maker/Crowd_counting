첫번째 오류

ValueError: Exception encountered when calling layer "sequential" (type Sequential).

==> 내가 설정해놓은 train test data와 모델에서 요구하는 데이터의 차원이 달라서 발생한 오류인 것 같다. 이를 해결하기 위해서 나는

기존에 사용했던 두번째 모델을 활용해서 데이터 구조를 일치해줬다.

x_train, y_train,x_test,y_test --> ds_test, ds_valid 형태로 바꿔줬다.

​

두번째 오류

==> ds_test, ds_valid로 바꿔보니  일치하니 이런 오류가 발생하였다.

ValueError: Input 0 of layer "sequential_1" is incompatible with the layer: expected shape=(None, 480, 640, 3), found shape=(None, 299, 299, 3)

​

expected shape=(None, 480, 640, 3) 이것의 구조를 위의 사진처럼 바꿨더니 오류 없이 학습을 시작하였다.

.

.

.

.

.

.

.

​

.

.

.

​

​

이후


밑에 epoch 100으로 학습한것은 생략하고,

