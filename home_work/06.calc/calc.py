import re


def symbol_update(formula_str):
    """
    对多出的空格，+- -- 进行转换
    :param formula_str: 需要进行转换的公式
    :return:转换过后的公式
    """
    formula_str = formula_str.replace(" ", "")
    formula_str = formula_str.replace("+-", "-")
    formula_str = formula_str.replace("--", "+")
    return formula_str


def add_subtract(symbol, md_str):
    """
    计算加减
    :param symbol:加减符号
    :param md_str: 经过括号乘除计算后的值
    :return:经过加减计算的值
    """
    num = ""
    for index, element in enumerate(md_str):
        if num:
            if symbol[index - 1] == "+":
                num += float(element)
            elif symbol[index - 1] == "-":
                num -= float(element)
        else:
            num = float(element)
    return num


def multiplication_division(number_str):
    """
    计算乘除
    :param number_str:传入需要进行乘除计算的数字 ['9', '2*5/3', '7/3*99/4*2998', '10*568/14']
    :return:返回经过乘除计算后的值
    """
    for index, element in enumerate(number_str):
        if "*" in element or "/" in element:
            symbol = re.findall("[*/]", element)
            calc_list = re.split("[*/]", element)
            num = ""
            for i, e in enumerate(calc_list):
                # 判断num是否有值
                if num:
                    if symbol[i - 1] == "*":
                        num *= float(e)
                    elif symbol[i - 1] == "/":
                        num /= float(e)
                else:
                    # 第一次判断 num 为空时，将'2*5/3'其中的2赋值给num
                    num = float(e)
            number_str[index] = num
    return number_str


def connect_str(symbol, number_str):
    """
    把列表中这样的形式['-', '-'] ['1', '2*', '1388335.8476190479'] 跟后面的元素合并到一块
    :param symbol:计算符号
    :param number_str: 需要进行合并的公式
    :return:进行合并操作完的计算符号 和 公式
    """
    for index, element in enumerate(number_str):
        if element.endswith("*") or element.endswith("/"):
            # ['-', '-'] ['1', '2*', '1388335.8476190479'] --->>>['-'], ['1', '2*-1388335.8476190479']
            number_str[index] = element + symbol[index] + number_str[index + 1]
            del number_str[index + 1]
            del symbol[index]
    return symbol, number_str


def brackets_calculate(after_formula):
    """
    括号中的公式进行计算
    :param after_formula:经过re匹配后 第一个满足条件的括号公式
    :return:括号中公式最终的结算结果
    """
    # 去除传入公式的两边的括号()
    brackets_formula = re.sub("[()]", "", after_formula)
    change_formula = symbol_update(brackets_formula)
    # 获取其中的公式中的加减符号
    symbol = re.findall("[+-]", change_formula)
    # 获取公式其中的去除加减的公式先进行乘除运算
    number_str = re.split("[+-]", change_formula)
    if number_str[0] == "":
        number_str[1] = "-" + number_str[1]
        del symbol[0]
        del number_str[0]
    res = connect_str(symbol, number_str)
    symbol = res[0]
    number_str = res[1]
    #经过乘除后的公式
    after_md = multiplication_division(number_str)
    # 经过加减后的公式
    after_as = add_subtract(symbol, after_md)

    return after_as


#1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# 1 - 2 * ( (60-30 +-8.0 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
#   1 - 2 * ( (60-30 +-8.0 * 173545.88095238098) - (-4*3)/ (16-3*2) )
#1 - 2 * ( -1388337.0476190478 - (-4*3)/ (16-3*2) )
#1 - 2 * ( -1388337.0476190478 - -12.0/ (16-3*2) )
#1 - 2 * ( -1388337.0476190478 - -12.0/ 10.0 )
#1 - 2 * -1388335.8476190479


def calc():
    """
    循环计算含有括号的公式，得出最后的值，然后再与括号外的公式进行计算
    :return:null
    """
    formula = input("请输入计算公式：")
    while True:
        # 正则取出带有括号的公式
        after_formula = re.search("\([^()]+\)", formula)
        # 如果仍有带括号公式，就将该括号公式取出计算其最终值，然后将最终值替换至原先括号所在位置
        if after_formula:
            after_formula = after_formula.group()
            res = brackets_calculate(after_formula)
            formula = formula.replace(after_formula, str(res))
        else:
            res = brackets_calculate(formula)
            print(res)
            exit()

if __name__ == "__main__":
    calc()