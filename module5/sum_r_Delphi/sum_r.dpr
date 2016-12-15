program sum_r;
{$apptype console}

{����� ����� ���� t=(a^(2n+1))/((2n+1)!) � �������� ���������;
�� �������� ������� Z(15,10) ����� ��� ��������, ������� ����� -
����������� �� � ������ X(�������� �� �������).
� ������� X �������� ������� ������ � ������������ ��������.
������� ����� ����, ������� � ������.}

uses
  SysUtils;

const
  MaxX = 10;        // ������������ ����� ��������
  MaxY = 15;        // ������������ ����� �����
  MaxV = MaxX*MaxY; // ������������ ������ �������

var
  t:real;       // ����� ����
  y:real;       // ����������� ���� ����
  b:real;       // �����
  a:real;       // �������� � �������
  eps:real;     // �������� ����������
  i, j:word;    // �������� �����
  nx, ny:word;  // ������� �������
  nk: word;     // ������ �������
  n:word;       // ���������� ������ ������������������
  vmax: word;   // ������ ������������� �������� �������

  X:array[1..MaxV] of real;          // �������������� ������
  Z:array[1..MaxY,1..MaxX] of real;  // �������� �������


begin

  WriteLn('������� �������� a � ��������� ��������: ');
  ReadLn(a,eps);

  WriteLn('������� ������ ������� ����� ������: ');
  WriteLn('(����� ����� �� 1 �� ',MaxY,', �������� �� 1 �� ',MaxX,')');
  ReadLn(ny,nx);

  while (ny < 1) or (ny > MaxY) or (nx < 1) or (nx > MaxX) do
    begin
      WriteLn('������������ ����! ������� ��� ����� � �������� ��������');
      ReadLn(ny,nx);
    end;

  WriteLn('������� ������� (',ny,',',nx,') ���������:');
  for i := 1 to ny do
    begin
      for j := 1 to nx do
        Read(Z[i,j]);
    end;

  WriteLn;



  // ���������� ����� ���� t � ��������� eps
  t := 0; y := a; n := 0;
  repeat
    t := t + y;
    n := n + 2;
    y := y*a*a/(n*n+n);
  until abs(y) < eps;
  n := n div 2;



  // ������ ������� �� �������, ����������� ���������, ������� �����, � ������
  nk := 0; vmax := 1;
  for i := 1 to ny do
    for j := 1 to nx do
      if Z[i,j] > t then
        begin
          nk := nk + 1;
          X[nk] := Z[i,j];
        end;

  WriteLn(n,' ����� ������������������ ���� ����� � ����������� ���������;');
  WriteLn('����� ������������������ = ',t:9:7);
  WriteLn('��������� ���� ������������������ = ',y:-7);

  WriteLn;
  WriteLn('�������� �������:');
  // ���������� ����� �������
  for i := 1 to ny do
    begin
      for j := 1 to nx do
        Write(Z[i,j]:5:0,' ');
      WriteLn
    end;
  WriteLn;

  if nk > 0 then
    begin // ����� ���������� ������� � ��� ���������
      WriteLn('������ X:');
      for i := 1 to nk do
        Write(X[i]:0:0,' ');
      WriteLn;

      // ����� ������������� �������� �������
      for i := 1 to nk do
        if X[i] >= X[vmax] then vmax := i;

      // ����� ������� �������� � ������������
      b := X[vmax];
      X[vmax] := X[1];
      X[1] := b;

      WriteLn;
      WriteLn('������ X ����� ������ ������������� � ������� ���������:');
      for i := 1 to nk do
        Write(X[i]:0:0,' ');
      WriteLn;
    end
  else
    WriteLn('������ X ������');
  WriteLn;

  WriteLn('������� ����� ������� ��� ������...');
  ReadLn;
  ReadLn;

end.
