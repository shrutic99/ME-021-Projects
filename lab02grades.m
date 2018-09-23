t = input('Enter your test 1 grade: ');
r = input('Enter your test 2 grade: ');
f = input('Enter your final exam grade: ');

grade = t*(.3)+r*(.3)+f*(.4);

if grade > 60
    if grade > 70
        if grade > 80
            if grade >= 90
                disp('A')
            end
            if grade>=80 && grade<90
                disp('B')
            end
        end
        if grade >= 70 && grade<80
            disp('C')
        end
    end
    if grade>=60 && grade<70
        disp('D')
    end
elseif grade < 60
    disp('F')
end

    
