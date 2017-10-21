﻿## 게임 이미지 정의 ----- 봄봄!
#==배경
image bg 0 = ("dark.png")
image bg 1 = im.FactorScale("bgs-field closeup.jpg",2)
image bg 2 = im.FactorScale("bgs-field.jpg",3)
image bg 3 = im.FactorScale("bgs-grassland.jpg",6)
image bg 4 = im.FactorScale("bgs-home.jpg",2)
image bg 5 = im.FactorScale("bgs-paddy.jpg",3)
image bg 6 = im.FactorScale("bgs-town.jpg",2)
image bg 7 = im.FactorScale("sunsetland.png",2)





#==인물


# 게임 캐릭터 정의
define none = Character(None, kind = nvl, image = "bg")

#-나
define he = Character('나', color="#7BA518", image = "he")

image he = "ch/he/he_3.png"

image he wooden :
    "ch/he/he_3.png"
image he angry :
    "ch/he/he_3.png"
image he smile :
    "ch/he/he_3.png"
image he sad :
    "ch/he/he_3.png"

#점순
#부끄러운 표정
define she = Character('점순', color="#CE723D", image = "she")

image she :
    im.FactorScale("ch/she/she_3.png",0.6)

image she gloomy :
    "ch/she/she_3.png"
image she smile :
    "ch/she/she_3.png"
image she wooden :
    "ch/she/she_3.png"
image she angry :
    "ch/she/she_3.png"


#장인
#당황한 표정, 울상인 표정 
define jang = Character('장인어른', color="#BD5C24", image = "jang")

image jang angry : 
    "ch/jang/jang_3.png"
image jang noisy : 
    "ch/jang/jang_3.png"
image jang wooden : 
    "ch/jang/jang_3.png"
image jang smile : 
    "ch/jang/jang_3.png"
image jang : 
    "ch/jang/jang_3.png"



#아직 이미지 없는 엑스트라들
define cow = Character('소', color="#BD9424", image = "cow")
define gu = Character('구장', color="#B0D0D6", image = "gu")
define mung = Character('뭉태', color="#918EDB", image = "mung")





label start:

    scene bg 0
    menu:
        "봄봄을 읽어보신 적이 있으십니까?"
        "네, 있어요...":
            return
        "아직 없는뎅?":
            jump chapter1
        


# 게임 사이클-1 시작.---------------------------------
label chapter1:
    
    #1. 집 마당, 아침 
    stop music fadeout .3
    scene bg 1
    show he wooden at left

    he "장인님! 인젠 저……."
    
    show jang angry at right

    jang "이 자식아! 성례구 뭐구 미처 자라야지!"
    scene bg 1
    "이 자라야 한다는 것은 내가 아니라 장차 내 아내가 될 점순이의 키 말이다."
    "내가 여기에 와서 돈 한푼 안 받고 일하기를 삼 년 하고 꼬박이 일곱 달 동안을 했다. "
    "그런데도 미처 못 자랐다니까 이 키는 언제야 자라는 겐지 짜장 영문 모른다." 
    "일을 좀더 잘해야 한다든지 혹은 밥을 (많이 먹는다고 노상 걱정이니까) 좀 덜 먹어야 한다든지 하면 나도 얼마든지 할 말이 많다." 
    "하지만 점순이가 아직 어리니까 더 자라야 한다는 여기에는 어째 볼 수 없이 그만 벙벙하고 만다."
    
    scene bg 2
    "이래서 나는 애최 계약이 잘못된 걸 알았다."
    "이태면 이태, 삼 년이면 삼 년, 기한을 딱 작정하고 일을 했어야 원 할 것이다."
    "덮어놓고 딸이 자라는 대로 성례를 시켜 주마, 했으니 누가 늘 지키고 섰는 것도 아니고 그 키가 언제 자라는지 알 수 있는가."
    "그리고 난 사람의 키가 무럭무럭 자라는 줄만 알았지 붙박이 키에 모로만 벌어지는 몸도 있는 것을 누가 알았으랴." 
    "때가 되면 장인님이 어련하랴 싶어서 군소리 없이 꾸벅꾸벅 일만 해왔다. 그럼 말이다, 장인님이 제가 다 알아차려서, "
    show jang smile at center
    jang "어 참 너 일 많이 했다. 고만 장가들어라."
    hide jang fadeout .5
    "하고 살림도 내주고 해야 나도 좋을 것이 아니냐."
    "시치미를 딱 떼고 도리어 그런 소리가 나올까 봐서 지레 펄펄 뛰고 이 야단이다."
    "명색이 좋아 데릴사위지 일하기에 싱겁기도 할 뿐더러 이건 참 아무것도 아니다."

    
    
    "숙맥이 그걸 모르고 점순이의 키 자라기만 까맣게 기다리지 않았나."
    
    scene bg 4

    "언젠가는 하도 갑갑해서 자를 가지고 덤벼들어서 그 키를 한번 재 볼까 했다마는, 우리는 장인님이 내외를 해야 한다고 해서 마주 서 이야기도 한마디 하는 법 없다."
    "우물길에서 언제나 마주칠 적이면 겨우 눈어림으로 재보고 하는 것인데 그럴 적마다 나는 저만큼 가서,"
    show he angry at left
    he angry"제―미 키두!"
    
    show she at right
    '아무리 잘 봐야 내 겨드랑(다른 사람보다 좀 크긴 하지만) 밑에서 넘을락말락 밤낮 요 모양이다.'
    '개돼지는 푹푹 크는데 왜 이리도 사람은 안 크는지, 한동안 머리가 아프도록 궁리도 해보았다.'
    '아하, 물동이를 자꾸 이니까 뼈다귀가 움츠러드나 보다, 하고 내가 넌짓넌짓이 그 물을 대신 길어도 주었다.'
    '뿐만 아니라 나무를 하러 가면 서낭당에 돌을 올려놓고,'
    
    scene bg 4
    he wooden"점순이의 키 좀 크게 해줍소사. 그러면 담엔 떡 갖다 놓고 고사드립죠니까."
    
    
    '하고 치성도 한두 번 드린 것이 아니다.'
    '어떻게 돼먹은 킨지 이래도 막무가내니……'
    '그래 내 어저께 싸운 것이지 결코 장인님이 밉다든가 해서가 아니다.'

    #2 논밭, 밭두렁
    scene bg 5
    show he at left
    he angry"아이구 배야!" 
    show jang at right
    jang noisy"너 이 자식, 왜 또 이래 응?"
    
    he smile"배가 좀 아파서유!"
    
    jang angry"이 자식아, 일허다 말면 누굴 망해 놀 속셈이냐, 이 대가릴 까놀 자식?"
    
    
    '우리 장인님은 약이 오르면 이렇게 손버릇이 아주 못됐다.'
    '또 사위에게 이자식 저자식 하는 이놈의 장인님은 어디 있느냐.'
    '오죽해야 우리 동리에서 누굴 물론하고 그에게 욕을 안 먹는 사람은 명이 짜르다 한다.'
    '조그만 아이들까지도 그를 돌아세 놓고 욕필이(본 이름이 봉필이니까), 욕필이, 하고 손가락질을 할 만치 두루 인심을 잃었다.'
    '하나 인심을 정말 잃었다면 욕보다 읍의 배참봉 댁 마름으로 더 잃었다.'
    '번이 마름이란 욕 잘 하고 사람 잘 치고 그리고 생김 생기길 호박개 같아야 쓰는 거지만 장인님은 외양에 똑 됐다.'
    '장인께 닭 마리나 좀 보내지 않는다든가 애벌논 때 품을 좀 안 준다든가 하면 그해 가을에는 영락없이 땅이 뚝뚝 떨어진다.'
    '그러면 미리부터 돈도 먹고 술도 먹이고 안달재신으로 돌아치던 놈이 그 땅을 슬쩍 돌아앉는다.'
    '이 바람에 장인님 집 외양간에는 눈깔 커다란 황소 한 놈이 절로 엉금엉금 기어들고, 동리 사람들은 그 욕을 다 먹어 가면서도 그래도 굽신굽신하는 게 아닌가―---'
    '그러나 내겐 장인님이 감히 큰소리할 계제가 못 된다.'
    '뒷생각은 못 하고 뺨 한 개를 딱 때려 놓고는 장인님은 무색해서 덤덤히 쓴 침만 삼킨다.'
    ' 난 그 속을 퍽 잘 안다. 조금 있으면 갈도 꺾어야 하고 모도 내야 하고, 한창 바쁜 때인데 나 일 안 하고 우리집으로 그냥 가면 고만이니까. '
    '작년 이맘때도 트집을 좀 하니까 늦잠 잔다고 돌멩이를 집어던져서 자는 놈의 발목을 삐게 해놨다.'
    '사날씩이나 건숭 끙, 끙, 앓았더니 종당에는 거반 울상이 되지 않았는가.'
    scene bg 6
    show jang at center
    jang noisy "얘, 그만 일어나 일 좀 해라. 그래야 올 갈에 벼 잘 되면 너 장가들지 않니."
    show he at left
    he smile "!!!!"

    hide he
    jang noisy "이 자식아 미처 커야지. 조걸 무슨 혼인을 한다고 그러니 원!"
    
    '하고 남 낯짝만 붉게 해주고 고만이다.'
    '골김에 그저 이놈의 장인님, 하고 댓돌에다 메꽂고 우리 고향으로 내뺄까 하다가 꾹꾹 참고 말았다.'
    
    '참말이지 난 이 꼴 하고는 집으로 차마 못 간다. 장가를 들러 갔다가 오죽 못났어야 그대로 쫓겨 왔느냐고 손가락질을 받을 테니까……. '
    
    scene bg 4
    show he at left
    he angry "난 갈 테야유, 그 동안 사경 쳐내슈"
    show jang at right
    jang angry "너 사위로 왔지 어디 머슴 살러 왔니?"
    
    he sad "그러면 얼찐 성례를 해줘야 안 하지유. 밤낮 부려만 먹구 해준다 해준다……."
    
    
    jang wooden "글쎄 내가 안 하는 거냐? 그년이 안 크니까……"
    

    '이렇게 따져 나가면 언제든지 늘 나만 밑지고 만다. 이번엔 안 된다 하고 대뜸 구장님한테로 판단 가자고 소맷자락을 내끌었다.'
    
    jang wooden "아 이 자식아, 왜 이래 어른을."
    
    '그러나 내 사실 참 장인님이 미워서 그런 것은 아니다.'
    scene bg 3

    show he at left

    #3.논밭
    '그 전날 왜 내가 새고개 맞은 봉우리 화전밭을 혼자 갈고 있지 않았느냐.'
    '밭 가생이로 돌 적마다 야릇한 꽃내가 물컥물컥 코를 찌르고 머리 위에서 벌들은 가끔 붕, 붕, 소리를 친다.'
    '바위 틈에서 샘물 소리밖에 안 들리는 산골짜기니까 맑은 하늘의 봄볕은 이불 속같이 따스하고 꼭 꿈꾸는 것 같다.' 
    '나는 몸이 나른하고(몸살을 아직 모르지만) 병이 나려고 그러는지 가슴이 울렁울렁하고 이랬다.'
    show he smile at left
    he smile "이러이! 말이! 맘 마 마……."
    
    '이렇게 노래를 하며 소를 부리면 여느 때 같으면 어깨가 으쓱으쓱한다.'
    '웬일인지 밭 반도 갈지 않아서 온몸의 맥이 풀리고 대고 짜증만 난다. 공연히 소만 들입다 두들기며, '
    
    he angry "안야! 안야! 이 망할자식의 소(장인님의 소니까) 대리를 꺾어 줄라."
    
    '점순이는 뭐 그리 썩 예쁜 계집애는 못 된다.' 
    '그렇다구 개떡이냐 하면 그런 것도 아니고, 꼭 내 아내가 돼야 할 만치 그저 툽툽하게 생긴 얼굴이다.'
    '나보다 십 년이 아래니까 올해 열여섯인데 몸은 남보다 두 살이나 덜 자랐다.' 
    '남은 잘도 훤칠히들 크건만 이건 위아래가 몽툭한 것이 내 눈에는 헐없이 감참외 같다.' 
    '참외 중에는 감참외가 제일 맛 좋고 예쁘니까 말이다.'
    '둥글고 커단 눈은 서글서글하니 좋고 좀 지쳐 찢어졌지만 입은 밥술이나 톡톡히 먹음직하니 좋다.' 
    '아따 밥만 많이 먹게 되면 팔자는 고만 아니냐. '
    '한데 한 가지 파가 있다면 가끔가다 몸이(장인님은 이걸 채신이 없이 들까분다고 하지만) 너무 빨리빨리 논다.' 
    '그래서 밥을 나르다가 때없이 풀밭에서 깻박을 쳐서 흙투성이 밥을 곧잘 먹인다.' 
    '안 먹으면 무안해할까 봐서 이걸 씹고 앉았노라면 으적으적 소리만 나고 돌을 먹는 겐지 밥을 먹는 겐지……. '
    
    cow "무우! 무우!"
    
    #3. 밭두렁, 밥그릇 있음
    show she at right
    '그러나 이날은 웬일인지 성한 밥채로 밭머리에 곱게 내려놓았다.'
    '그리고 또 내외를 해야 하니까 저만큼 떨어져 이쪽으로 등을 향하고 웅크리고 앉아서 그릇 나기를 기다린다.'
    '내가 다 먹고 물러섰을 때 그릇을 와서 챙기는데, 그런데 난 깜짝 놀라지 않았느냐.' 
    '고개를 푹 숙이고 밥함지에 그릇을 포개면서 날더러 들으라는지 혹은 제 소린지,'
    
    she wooden "밤낮 일만 하다 말 텐가!" 

    '하고 혼자 쫑알거린다.'
    '고대 잘 내외하다가 이게 무슨 소린가, 하고 난 정신이 얼떨떨했다.' 
    '그러면서도 한편 무슨 좋은 수가 있는가 싶어서 나도 공중을 대고 혼자말로,'
    
    he sad "그럼 어떡해?"
    
    '라고 하니까'
    
    she wooden"성례시켜 달라지 뭘 어떡해……."
    
    '하고 되알지게 쏘아붙이고 얼굴이 발개져서 산으로 그저 도망질을 친다. '
    
    '나는 잠시 동안 어떻게 되는 셈판인지 맥을 몰라서 그 뒷모양만 덤덤히 바라보았다.'
    
    '봄이 되면 온갖 초목이 물이 오르고 싹이 트고 한다.' 
    '사람도 아마 그런가 보다, 하고 며칠 내에 부쩍(속으로) 자란 듯싶은 점순이가 여간 반가운 것이 아니다. '
    
    '이런 걸 멀쩡하게 안직 어리다구 하니까……. '
    scene bg 6
    #4. 구장 집 마당
    '우리가 구장님을 찾아갔을 때 그는 싸리문 밖에 있는 돼지우리에서 죽을 퍼주고 있었다.' 
    '서울엘 좀 갔다 오더니 사람은 점잖아야 한다고 웃쇰이(얼른 보면 지붕 위에 앉은 제비 꼬랑지 같다) 양쪽으로 뾰족이 뻗치고 그걸 에헴, 하고 늘 쓰다듬는 손버릇이 있다.' 
    '우리를 멀뚱히 쳐다보고 미리 알아챘는지,'
    
    
    gu "왜 일들 허다 말구 그래?"
    
    '하더니 손을 올려서 그 에헴을 한번 후딱 했다.'
    show he angry at left
    he angry"구장님! 우리 장인님과 츰에 계약하기를……."
    '먼저 덤비는 장인님을 뒤로 떠다밀고 내가 허둥지둥 달려들다가 가만히 생각하고, '
    
    he wooden "아니 우리 빙장님과 츰에."
    
    '하고 첫번부터 다시 말을 고쳤다. 장인님은 빙장님 해야 좋아하고 밖에 나와서 장인님 하면 괜스레 골을 내려 든다.' 
    '뱀두 뱀이래야 좋으냐구 창피스러우니 남 듣는 데는 제발 빙장님, 빙모님, 하라구 일상 당조짐을 받아 오면서 난 그것도 자꾸 잊는다.'
    '당장도 장인님 하다 옆에서 내 발등을 꾹 밟고 곁눈질을 흘기는 바람에야 겨우 알았지만……. '
    
    
    '구장님도 내 이야기를 자세히 듣더니 퍽 딱한 모양이었다.' 
    '하기야 구장님뿐만 아니라 누구든지 다 그럴 게다.' 
    '길게 길러 둔 새끼손톱으로 코를 후벼서 저리 탁 튀기며, '
    
    gu  "그럼 봉필 씨! 얼른 성례를 시켜 주구려, 그렇게까지 제가 하구 싶다는 걸……."
    '하고 내 짐작대로 말했다. 그러나 이 말에 장인님은 삿대질로 눈을 부라리고,  '
    show jang angry at right
    hide he
    jang angry "아 성례구 뭐구 계집애년이 미처 자라야 할 게 아닌가?"
    '하니까 고만 멀쑤룩해서 입맛만 쩍쩍 다실 뿐이 아닌가. '
    gu "그것두 그래!"
    show he angry at left
    he wooden "그래, 거진 사 년 동안에도 안 자랐다니 그 킨 은제 자라지유? 다 그만두구 사경 내슈……."
    jang angry "글쎄, 이 자식아! 내가 크질 말라구 그랬니, 왜 날 보구 떼냐?"
    he wooden "빙모님은 참새만한 것이 그럼 어떻게 앨 낳지유?(사실 장모님은 점순이보다도 귀때기 하나가 작다.)" 
    '장인님은 이 말을 듣고 껄껄 웃더니(그러나 암만해두 돌 씹은 상이다) 코를 푸는 척하고 날 은근히 곯리려고 팔꿈치로 옆 갈비께를 퍽 치는 것이다.' 
    '더럽다.'
    '나도 종아리의 파리를 쫓는 척하고 허리를 구부리며 그 궁둥이를 콱 떼밀었다.' 
    '장인님은 앞으로 우찔근하고 싸리문께로 쓰러질 듯하다 몸을 바로 고치더니 눈총을 몹시 쏘았다.' 
    '이런 상년의 자식! 하곤 싶으나 남의 앞이라서 차마 못 하고 섰는 그 꼴이 보기에 퍽 쟁그라웠다. '
    '그러나 이 밖에는 별반 신통한 귀정을 얻지 못하고 도로 논으로 돌아와서 모를 부었다.' 
    '왜냐면 장인님이 뭐라고 귓속말로 수군수군하고 간 뒤다.'
    '구장님이 날 위해서 조용히 데리고 아래와 같이 일러 주었기 때문이다. '
    '(뭉태의 말은 구장님이 장인님에게 땅 두 마지기 얻어 부치니까 그래 꾀었다고 하지만 난 그렇게 생각 않는다.)'

    hide he
    hide jang

    gu "자네 말두 하기야 옳지, 암 나이찼으니까 아들이 급하다는 게 잘못된 말은 아니야." 
    "허지만 농사가 한창 바쁜 때 일을 안 한다든가 집으로 달아난다든가 하면 손해죄루 그것두 징역을 가거든! 
    (여기에 그만 정신이 번쩍 났다.)"
    "왜 요전에 삼포말서 산에 불 좀 놓았다구 징역 간 거 못 봤나?"
    "제 산에 불을 놓아도 징역을 가는 이땐데 남의 농사를 버려 주니 죄가 얼마나 더 중한가."
    "그리고 자넨 정장을(사경 받으러 정장 가겠다 했다) 간대지만 그러면 괜시리 죄를 들쓰고 들어가는 걸세." 
    "또 결혼두 그렇지, 법률에 성년이란 게 있는데 스물하나가 돼야 비로소 결혼을 할 수 있는 걸세."
    "자넨 물론 아들이 늦을 걸 염려하지만 점순이루 말하면 이제 겨우 열여섯이 아닌가. "
    "그렇지만 아까 빙장님의 말씀이 올 갈에는 열일을 제치고라두 성례를 시켜 주겠다 하니 좀 고마울 겐가." 
    "빨리 가서 모 붓던 거나 마저 붓게, 군소리 말구 어서 가."
    scene bg 5
    #물음표 같은 표정
    he angry '그래서 오늘 아침까지 끽소리 없이 왔다.'
    '장인님과 내가 싸운 것은 지금 생각하면 뜻밖의 일이라 안 할 수 없다.' 
    '장인님으로 말하면 요즈막 작인들에게 행세를 좀 하고 싶다고 해서 -돈 있으면 양반이지 별게 있느냐!- 하고 일부러 아랫배를 툭 내밀고 걸음도 뒤틀리게 걷고 하는 이 판이다.' 
    '이까짓 나쯤 두들기다 남의 땅을 가지고 모처럼 닦아 놓았던 가문을 망친다든지 할 어른이 아니다.' 
    '또 나로 논지면 아무쪼록 잘 봬서 점순이에게 얼른 장가를 들어야 하지 않느냐. '
    
    mung "그래 맞구두 그걸 가만둬?" 
    #궁금한 표정
    show he at left
    he wooden "그럼 어떡하니?" 
    mung "임마 봉필일 모판에다 거꾸루 박아 놓지 뭘 어떡해?"
    
    '하고 괜히 내 대신 화를 내가지고 주먹질을 하다 등잔까지 쳤다.' 
    '놈이 본시 괄괄은 하지만 그래 놓고 날더러 석윳값을 물라고 막 지다위를 붙는다.' 
    '난 어안이 벙벙해서 잠자코 앉았으니까 저만 연방 지껄이는 소리가, '
    
    mung "밤낮 일만 해주구 있을 테냐?"
    mung "영득이는 일 년을 살구도 장갈 들었는데 난 사 년이나 살구두 더 살아야 해."
    mung "네가 세 번째 사윈 줄이나 아니? 세 번째 사위."
    mung "남의 일이라두 분하다 이 자식아, 우물에 가 빠져 죽어."

    '나중에는 겨우 손톱으로 목을 따라고까지 하고 제 아들같이 함부로 훅닥이었다.' 
    '별의별 소리를 다 해서 그대로 옮길 수는 없으나 그 줄거리는 이렇다.'
    '우리 장인님이 딸이 셋이 있는데 맏딸은 재작년 가을에 시집을 갔다.' 
    '정말은 시집을 간 것이 아니라 그 딸도 데릴사위를 해가지고 있다가 내보냈다.' 
    '그런데 딸이 열살 때부터 열아홉, 즉 십 년 동안에 데릴사위를 갈아 들이기를, 동리에선 사위 부자라고 이름이 났지마는 열 놈이란 참 너무 많다.'
    '장인님이 아들은 없고 딸만 있는 고로 그 담 딸을 데릴사위를 해올 때까지는 부려먹지 않으면 안 된다.' 
    '물론 머슴을 두면 좋지만 그건 돈이 드니까, 일 잘하는 놈을 고르느라고 연방 바꿔 들였다.' 
    '또 한편 놈들이 욕만 줄창 퍼붓고 심히도 부려먹으니까 밸이 상해서 달아나기도 했겠지. '
    '점순이는 둘째딸인데 내가 일테면 그 세 번째 데릴사위로 들어온 셈이다. '
    '내 담으로 네 번째 놈이 들어올 것을 내가 일도 참 잘하고 그리고 사람이 좀 어수룩하니까 장인님이 잔뜩 붙들고 놓질 않는다.'
    '셋째딸이 인제 여섯 살, 적어두 열 살은 돼야 데릴사위를 할 테므로 그 동안은 죽도록 부려먹어야 된다. '
    '그러니 인제는 속 좀 차리고 장가를 들여 달라구 떼를 쓰고 나자빠져라, 이것이다. '

    '나는 건성으로 엉, 엉, 하며 귓등으로 들었다.' 
    '뭉태는 땅을 얻어 부치다가 떨어진 뒤로는 장인님만 보면 공연히 못 먹어서 으릉거린다.' 
    '그것도 장인님이 저 달라고 할 적에 제 집에서 위한다는 그 감투(예전에 원님이 쓰던 것이라나, 옆구리에 뽕뽕 좀먹은 걸레)를 선뜻 주었더라면 그럴 리도 없었던 걸…….' 

    '그러나 나는 뭉태란 놈의 말을 전수이 곧이듣지 않았다.'
    '꼭 곧이들었다면 간밤에 와서 장인님과 싸웠지 무사히 있었을 리가 없지 않은가. '
    '그러면 딸에게까지 인심을 잃은 장인님이 혼자 나빴다. '
    scene bg 1
    '실토이지 나는 점순이가 아침상을 가지고 나올 때까지는 오늘은 또 얼마나 밥을 담았나, 하고 이것만 생각했다.' 
    '상에는 된장찌개하고 간장 한 종지, 조밥 한 그릇, 그리고 밥보다 더 수부룩하게 담은 산나물이 한 대접, 이렇다.' 
    '나물은 점순이가 틈틈이 해오니까 두 대접이고 네 대접이고 멋대로 먹어도 좋으나 밥은 장인님이 한 사발 외엔 더 주지 말라고 해서 안 된다.'
    '그런데 점순이가 그 상을 내 앞에 내놓으며 제 말로 지껄이는 소리가, '
    show she at right
    she angry "구장님한테 갔다 그냥 온담 그래!" 
    '하고 엊그제 산에서와 같이 되우 쫑알거린다.' 
    '딴은 내가 더 단단히 덤비지 않고 만 것이 좀 어리석었다, 속으로 그랬다.' 
    '나도 저쪽 벽을 향하여 외면하면서 내 말로, '
    show he angry at left
    #살짝 짜증난듯
    he wooden "안 된다는 걸 그럼 어떡헌담!"
    she angry "쇰을 잡아 채지 그냥 둬, 이 바보야!"
    
    '하고 또 얼굴이 빨개지면서 성을 내며 안으로 샐죽하니 튀들어 가지 않느냐. '
    '이때 아무도 본 사람이 없었게망정이지 보았다면 내 얼굴이 어미 잃은 황새새끼처럼 가엾다, 했을 것이다. '

    '사실 이때만큼 슬펐던 일이 또 있었는지 모른다. '
    '다른 사람은 암만 못생겼다 해도 괜찮지만 내 아내 될 점순이가 병신으로 본다면 참 신세는 따분하다. '
    '밥을 먹은 뒤 지게를 지고 일터로 가려 하다 도로 벗어 던지고 바깥 마당 공석 위에 드러누워서 나는 차라리 죽느니만 같지 못하다 생각했다.'

    '내가 일 안 하면 장인님 저는 나이가 먹어 못 하고 결국 농사 못 짓고 만다.'
    '뒷짐으로 트림을 꿀꺽, 하고 대문 밖으로 나오다 날 보고서,'
    
    jang "이 자식아! 너 왜 또 이러니?"
    #아프다자나 아픈표정
    he wooden "관격이 났어유, 아이구 배야!"
    jang angry "기껀 밥 처먹고 나서 무슨 관격이야, 남의 농사 버려 주면 이 자식아 징역 간다 봐라!"
    he wooden "가두 좋아유, 아이구 배야!"
    
    '참말 난 일 안 해서 징역 가도 좋다 생각했다.' 
    '일후 아들을 낳아도 그 앞에서 바보 바보 이렇게 별명을 들을 테니까 오늘은 열 쪽이 난대도 결정을 내고 싶었다.' 

    '장인님이 일어나라고 해도 내가 안 일어나니까 눈에 독이 올라서 저편으로 힝 하게 가더니 지게 막대기를 들고 왔다.' 
    '그리고 그걸로 내 허리를 마치 들떠 넘기듯이 쿡 찍어서 넘기고 넘기고 했다.' 
    '밥을 잔뜩 먹고 딱딱한 배가 그럴 적마다 퉁겨지면서 밸창이 꼿꼿한 것이 여간 켕기지 않았다.' 
    '그래도 안 일어나니까 이번엔 배를 지게 막대기로 위에서 쿡쿡 찌르고 발길로 옆구리를 차고 했다.' 
    '장인님은 원체 심청이 궂어서 그렇지만 나도 저만 못하지 않게 배를 채었다.' 
    '아픈 것을 눈을 꽉 감고 넌 해라 난 재미단 듯이 있었으나 볼기짝을 후려갈길 적에는 나도 모르는 결에 벌떡 일어나서 그 수염을 잡아챘다마는,'
    '내 골이 난 것이 아니라 정말은 아까부터 부엌 뒤 울타리 구멍으로 점순이가 우리들의 꼴을 몰래 엿보고 있었기 때문이다.' 
    '가뜩이나 말 한마디 톡톡히 못 한다고 바보라는데 매까지 잠자코 맞는 걸 보면 짜장 바보로 알 게 아닌가.' 
    '또 점순이도 미워하는 이까짓 놈의 장인님 나하곤 아무것도 안 되니까 막 때려도 좋지만 사정 보아서 수염만 채고(제 원대로 했으니까 이때 점순이는 퍽 기뻤겠지) 저기까지 잘 들리도록,'
    
    he angry "이걸 까셀라 부다!" 
    he angry "부려만 먹구 왜 성례 안 하지유!" 
    
    '하고 소리를 쳤다.' 
    '장인님은 더 약이 바짝 올라서 잡은 참 지게 막대기로 내 어깨를 그냥 내리갈겼다.'
    '정신이 다 아찔하다. '
    '다시 고개를 들었을 때 그때엔 나도 온몸에 약이 올랐다. '
    '이 녀석의 장인님을, 하고 눈에서 불이 퍽 나서 그 아래 밭 있는 넝 알로 그대로 떠밀어 굴려 버렸다. '
    '조금 있다가 장인님이 씩, 씩, 하고 한번 해보려고 기어오르는 걸 얼른 또 떠밀어 굴려 버렸다. '

    '기어오르면 굴리고, 굴리면 기어오르고, 이러길 한 너덧 번을 하며 그럴 적마다, '

    he angry "부려만 먹구 왜 성례 안 하지유!" 
    
    '나는 이렇게 호령했다.' 
    '하지만 장인님이 선뜻, 오냐 낼이라두 성례시켜 주마, 했으면 나도 성가신 걸 그만두었을지 모른다. '
    '나야 이러면 때린 건 아니니까 나중에 장인 쳤다는 누명도 안 들을 터이고 얼마든지 해도 좋다.'
    '한번은 장인님이 헐떡헐떡 기어서 올라오더니 내 바짓가랑이를 요렇게 노리고서 단박 움켜잡고 매달렸다.' 
    '악, 소리를 치고 나는 그만 세상이 다 팽그르 도는 것이,'
        
    #이게 슬픈건가?    
    he sad "빙장님! 빙장님! 빙장님!" 
    jang angry "이 자식! 잡아먹어라. 잡아먹어!" 
    #으아ㅏ아아ㅏ
    he sad "아! 아! 할아버지! 살려 줍쇼, 할아버지!" 
        
    '하고 두 팔을 허둥지둥 내절 적에는 이마에 진땀이 쭉 내솟고 인젠 참으로 죽나 보다, 했다.' 
    '그래도 장인님은 놓질 않더니 내가 기어이 땅바닥에 쓰러져서 거진 까무러치게 되니까 놓는다.'
    '더럽다. 더럽다. '
    '이게 장인님인가, 나는 한참을 못 일어나고 쩔맸다. '
    '그러다, 얼굴을 드니(눈에 참 아무것도 보이지 않았다) 사지가 부르르 떨리면서 나도 엉금엉금 기어가 장인님의 바짓가랑이를 꽉 움키고 잡아나꿨다.'

    '내가 머리가 터지도록 매를 얻어맞은 것이 이 때문이다. 그러나 여기가 또한 우리 장인님이 유달리 착한 곳이다.' 
    '여느 사람이면 사경을 주어서라도 당장 내쫓았지 터진 머리를 볼솜으로 손수 지져 주고, 호주머니에 희연 한 봉을 넣어 주시고 그리고, '
        
    jang angry " 올 갈엔 꼭 성례를 시켜 주마. 암말 말구 가서 뒷골의 콩밭이나 얼른 갈아라." 
    he sad "빙장님! 인제 다시는 안 그러겠어유." 
    '하고 등을 뚜덕여 줄 사람이 누구냐.' 

    '나는 장인님이 너무나 고마워서 어느덧 눈물까지 났다.' 
    '점순이를 남기고 이젠 내쫓기려니, 하다 뜻밖의 말을 듣고, '
        
    he sad "빙장님! 인제 다시는 안 그러겠어유."
        
    '이렇게 맹세를 하며 부랴사랴 지게를 지고 일터로 갔다.' 

    '그러나 이때는 그걸 모르고 장인님을 원수로만 여겨서 잔뜩 잡아당겼다. '

    jang angry "아! 아! 이놈아! 놔라, 놔." 
    '장인님은 헛손질을 하며 솔개미에 챈 닭의 소리를 연해 질렀다.' 
    '놓긴 왜, 이왕이면 호되게 혼을 내주리라.'
    '그렇게 생각하고 짓궂이 더 댕겼다마는, 장인님이 땅에 쓰러져서 눈에 눈물이 피잉 도는 것을 알고 좀 겁도 났다. '
        
    jang angry " 할아버지! 놔라, 놔, 놔, 놔놔." 
        
    '그래도 안되니까 화나서'
        
    jang angry "얘 점순아! 점순아!" 

    '이 악장에 안에 있었던 장모님과 점순이가 헐레벌떡하고 단숨에 뛰어나왔다.' 

    '나의 생각에 장모님은 제 남편이니까 역성을 할는지도 모른다.'
    '그러나 점순이는 내 편을 들어서 속으로 고소해서 하겠지―라고 생각했다.'
    '그러나 대체 이게 웬 속인지(지금까지도 난 영문을 모른다) 아버질 혼내 주기는 제가 내래 놓고 이제 와서는 달려들며, '
        
    she angry "에그머니! 이 망할 게 아버지 죽이네!" 
        
    '하고 내 귀를 뒤로 잡아당기며 마냥 우는 것이 아니냐.' 
    '그만 여기에 기운이 탁 꺾이어 나는 얼빠진 등신이 되고 말았다.' 
    '장모님도 덤벼들어 한쪽 귀마저 뒤로 잡아 채면서 또 우는 것이다.' 

    '이렇게 꼼짝도 못하게 해놓고 장인님은 지게 막대기를 들어서 사뭇 내려조겼다.' 
    '그러나 나는 구태여 피하려지도 않고 암만해도 그 속 알 수 없는 점순이의 얼굴만 멀거니 들여다보았다. '
        
        
        
    jang angry "이 자식! 장인 입에서 할아버지 소리가 나오도록 해?"
        
        
        
    
    return
