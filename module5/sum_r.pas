program sum_r;
{$apptype console}

{Найти сумму ряда t=(a^(2n+1))/((2n+1)!) с заданной точностью;
во введённой матрице Z(15,10) найти все элементы, большие суммы -
скопировать их в вектор X(просмотр по строкам).
В векторе X обменять местами первый и максимальный элементы.
Вывести сумму ряда, матрицу и вектор.}

uses
  SysUtils;

const
  MaxX = 10;        // Максимальное число столбцов
  MaxY = 15;        // Максимальное число строк
  MaxV = MaxX*MaxY; // Максимальный размер вектора

var
  t:real;       // Сумма ряда
  y:real;       // Вычисляемый член ряда
  b:real;       // Буфер
  a:real;       // Параметр а формулы
  eps:real;     // Точность вычисления
  i,j:word;     // Счётчики цикла
  nx, ny:word;  // Размеры матрицы
  nk: word;     // Размер вектора
  n:word;       // Количество членов последовательности
  vmax: word;   // Индекс максимального элемента вектора

  X:array[1..MaxV] of real;          // Вектор X(150)
  Z:array[1..MaxY,1..MaxX] of real;  // Матрица X(15,10)


begin

  WriteLn('Задайте параметр a и требуемую точность: ');
  ReadLn(a,eps);

  Write('Задайте число строк и столбцов матрицы: ');
  ReadLn(ny,nx);

  WriteLn('Введите матрицу (',ny,',',nx,') построчно:');
  for i := 1 to ny do begin
    for j := 1 to nx do
      Read(Z[i,j]);
  end;

  WriteLn;



  // Вычисление суммы ряда t с точностью eps
  t := 0; y := a; n := 0;
  repeat
    t := t + y;
    n := n + 2;
    y := y*a*a/(n*n+n);
  until abs(y) < eps;
  n := n div 2;



  // Проход матрицы по строкам, копирование элементов, больших суммы, в вектор
  nk := 0; vmax := 1;
  for i := 1 to ny do
    for j := 1 to nx do
      if Z[i,j] > t then
      begin
        nk := nk + 1;
        X[nk] := Z[i,j];
      end;

  WriteLn(n,' члена(-ов) последовательности дают сумму с необходимой точностью;');
  WriteLn('Сумма последовательности = ',t:0:7);
  WriteLn('Следующий член последовательности = ',y:0:7);

  WriteLn;
  WriteLn('Исходная матрица:');
  // Построчный вывод матрицы
  for i := 1 to ny do
  begin
    for j := 1 to nx do
      Write(Z[i,j]:0:5,' ');
    WriteLn
  end;
  WriteLn;

  if nk > 0 then begin // Вывод ненулевого вектора и его обработка
    WriteLn('Вектор X:');
    for i := 1 to nk do
      Write(X[i]:0:5,' ');
    WriteLn;

    // Поиск максимального элемента вектора
    for i := 1 to nk do
      if X[i] >= X[vmax] then vmax := i;

    // Обмен первого элемента с максимальным
    b := X[vmax];
    X[vmax] := X[1];
    X[1] := b;

    WriteLn;
    WriteLn('Вектор X после обмена местами максимального и первого элементов:');
    for i := 1 to nk do
      Write(X[i]:0:5,' ');
    WriteLn;

    end
  else
    WriteLn('Вектор X пустой');
  WriteLn;

  WriteLn('Нажмите любую клавишу для выхода...');
  ReadLn;
  ReadLn;

end.
