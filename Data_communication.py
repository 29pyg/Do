import glob, csv
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:     # Construct a file object
            csv_reader = csv.reader(f) # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'): # If 'line' is valid and not a header
                    data.append([int(val) for val in line])      # Append 'line' to 'data' as numbers
            all_data = all_data + data                           # Merge 'data' to 'all_data'
    return all_data

if __name__ == '__main__':
    class_data = read_data('data/data_communication.csv')

    midtm_data = [row[0]for row in class_data]
    final_data = [row[1]for row in class_data]
    total_data = [row[0]*50/100+ row[1]*50/100 for row in class_data]

    plt.plot(midtm_data, final_data, 'b+',label='Score')
    plt.xlabel('Midterm Exam')
    plt.ylabel('Final Exam')
    plt.legend()

    plt.figure()
    plt.hist(total_data, range=(0,100), bins=20, color='b', alpha=1)
    
    scores = np.array(read_data('data/data_communication.csv'))
    midtm_range = np.array([0, 100])
    final_range = np.array([0, 100])
                                                 
    A= np.vstack((scores[:,0], np.ones(len(scores)))).T
    b=scores[:,1]
    line = np.matmul(np.linalg.pinv(A),b)
    
    # Predict scores
    final = lambda midterm: line[0] * midterm + line[1]
    while True:
        given = float(input('중간고사 점수를 입력하세요 (취소: -1)? '))
        if given < 0:
            break
        print(f'예상되는 기말고사 점수는 {final(given):.3f}. 점 입니다.')

    # Plot scores and the estimated line
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
    
    