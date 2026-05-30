# Want percentage for each subject along with marks, and overall percentage with overall marks after all inputs. In beautifully formatted data.

def percentage():
    num_subjects = int(input("Enter the number of subjects: "))
    
    subjects_data = []
    total_obtained_all = 0
    total_max_all = 0
    
    for i in range(num_subjects):
        sub_name = input(f"Enter the name of subject {i + 1}: ")
        obtained = int(input(f"Enter obtained marks for {sub_name}: "))
        total = int(input(f"Enter total marks for {sub_name}: "))
        
        sub_percentage = (obtained / total) * 100 if total > 0 else 0
        
        subjects_data.append({
            'name': sub_name,
            'obtained': obtained,
            'total': total,
            'percentage': sub_percentage
        })
        
        total_obtained_all += obtained
        total_max_all += total
        
    print("\n                 ***** Your result *****\n")
    
    for data in subjects_data:
        marks_str = f"{data['obtained']}/{data['total']}"
        print(f"        {data['name']:<22} {marks_str:<10} {data['percentage']:>6.2f}%")
        
    print("        " + "-" * 42)
    
    overall_percentage = (total_obtained_all / total_max_all) * 100 if total_max_all > 0 else 0
    overall_marks_str = f"{total_obtained_all}/{total_max_all}"
    
    print(f"        {'OVERALL TOTAL':<22} {overall_marks_str:<10} {overall_percentage:>6.2f}%\n")
    
    return overall_percentage

percentage()