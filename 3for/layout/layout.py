def input_space(input_space_w):
    # for input
    box = []
    box = [int(i) for i in raw_input().split(' ')]
    box_w = box[0]
    box_h = box[1]
    layout(box_w, box_h, input_space_w)
    return box_w, box_h, input_space_w


def layout(box_w, box_h, input_space_w):
    # when each loop, left
    left_space_w = input_space_w
    # output
    max_w = 0
    max_h = 0
    current_h = 0
    line_location_h = 0
    # input each box
    while box_w != -1 and box_h != -1:
        # when need to make height space
        if left_space_w < box_w:
            # get new line of left_space_w
            left_space_w = input_space_w - box_w
            line_location_h = max_h
            max_h += box_h
            current_h = max_h
            #print '26 max_h', max_h
            # is max_w is max of all line width
            if max_w <= box_w:
                max_w = box_w
        # when no need to make next space
        else:
            left_space_w -= box_w
            # when adding box_w, is max_w smaller than used_space_w
            if max_w <= input_space_w - left_space_w:
                max_w = input_space_w - left_space_w
            if current_h < line_location_h + box_h:
                current_h = line_location_h + box_h
            if max_h <= current_h:
                max_h = current_h
                #print '41 max_h', max_h
            #print '43 current_h', current_h
        # for input
        box = []
        box = [int(i) for i in raw_input().split(' ')]
        box_w = box[0]
        box_h = box[1]
    print max_w, 'x', max_h
    return max_w, max_h


input_space_w = input()
input_space(int(input_space_w))
