def solution(players, callings):
    d = {name:i for i,name in enumerate(players)} # 이름: 순위 딕셔너리 생성
    for name in callings:
        pre, cur = d[name]-1, d[name] # 불린 이름의 순위를 받아와서
        players[pre], players[cur] = players[cur], players[pre] # 현재 선수의 순서를 바꿔줌
        d[players[pre]], d[players[cur]] = d[players[pre]]-1, d[players[cur]]+1 #순위 딕셔너리 업데이트
    return players