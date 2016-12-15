program matrix;

{$APPTYPE CONSOLE}

uses
  SysUtils;

const
  N = 11;
  M = 8;

var
  B:array[1..N,1..M] of real;
  an, am, i, j, k, l:integer;
  flag:boolean;

begin
  WriteLn('������� ������� ������� (�� ',N,' �� ',M,'):');
  ReadLn(an,am);

  WriteLn('������� ������� (',an,';',am,') ���������:');
  for i := 1 to an do
    for j := 1 to am do
      Read(B[i,j]);
  WriteLn;

  WriteLn('�������� �������:');
  for i := 1 to an do
    begin
      for j := 1 to am do
        Write(B[i,j]:9:7,' ');
      WriteLn;
    end;
  WriteLn;

  i := 1;
  while i <= an do
    begin
      flag := true;
      for j := 1 to am do
        if B[i,j] <= 0 then
          flag := false;
        if flag then
          begin
            if (i <> an) then
              for k := i to an-1 do
                for l := 1 to am do
                  B[k,l] := B[k+1,l];
              an := an - 1;
              i := i - 1;
          end;
      i := i + 1;
    end;

  if an > 0 then
    begin
      WriteLn('���������� �������:');
      for i := 1 to an do
        begin
          for j := 1 to am do
            Write(B[i,j]:9:7,' ');
          WriteLn;
        end;
     end
   else
     WriteLn('��� �������� - �������������');

  WriteLn;
  WriteLn('Press any key to exit');
  ReadLn;
  ReadLn;
end.
