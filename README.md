서울과학기술대학교[SeoulTech](http://seoultech.ac.kr/) 컴퓨터공학과 학생 박이규 입니다.

이 수업은 오픈소스 프로그래밍 수업의 내용을 포함하고 있습니다.

모든 코드는 오픈소스프로그래밍 수업의 교수님이신 최성록 교수님의 과제 스켈레톤 코드를 바탕으로 제작되었습니다.

    midtm_data = [row[0]for row in class_data]
    final_data = [row[1]for row in class_data]
    total_data = [row[0]*50/100+ row[1]*50/100 for row in class_data]

    plt.plot(midtm_data, final_data, 'b+',label='English')
    plt.xlabel('Midterm Exam')
    plt.ylabel('Final Exam')
    plt.legend()

    plt.figure()
    plt.hist(total_data, range=(0,100), bins=20, color='b', alpha=1)


아래 그림은 위의 코드를 실행하여 나온 중간고사, 기말고사의 점수 분포 모양이다.
![333333333](https://user-images.githubusercontent.com/61642764/146812137-82f1f705-a53d-4ce4-8a48-2afcf930dcd0.PNG)


    scores = np.array(read_data('data/data_communication.csv'))
    midtm_range = np.array([0, 100])
    final_range = np.array([0, 100])
                                                 
    A= np.vstack((scores[:,0], np.ones(len(scores)))).T
    b=scores[:,1]
    line = np.matmul(np.linalg.pinv(A),b)
    
    final = lambda midterm: line[0] * midterm + line[1]
    while True:
        given = float(input('중간고사 점수를 입력하세요 (취소: -1)? '))
        if given < 0:
            break
        print(f'예상되는 기말고사 점수는 {final(given):.3f}. 점 입니다.')

아래 그림은 위의 코드를 실행하여 나온 질문에 자신에 중간고사 성적을 입력하여 기말고사 점수를 도출해줬다.
![2222222222](https://user-images.githubusercontent.com/61642764/146810058-824cc47c-f298-4af6-b958-44c7a427761e.PNG)

    plt.figure()
    plt.plot(scores[:,0], scores[:,1], 'r.', label='The given data')
    plt.plot(midtm_range, final(midtm_range), 'b-', label='Prediction')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim(midtm_range)
    plt.ylim(final_range)
    plt.grid()
    plt.legend()
    plt.show()

아래 그림은 위의 코드를 실행하여 중간고사, 기말고사 성적의 분포로 예측한 예측선이다. 
![1111111](https://user-images.githubusercontent.com/61642764/146810009-149a5727-f292-4c7f-9b58-403eeb1edbdc.PNG)
