import numpy as np

#an example of message to encode (should be string datatype)
message = 'Just for fun tra la la'

#the key variable is mutable. you need to use the same one for decoding of encoded messages (should be integer datatype (for this encoder edition))
key = 256


def enc(key, message):
    encoded_message = ''

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = alph.lower()
    non_alph = r'0123456789!"#$%&\'()*+,-./:;<=>?@ [\\]^_`{|}~'
    cho = []
    for a in alph:
        cho.append(a)
    for al in alph_low:
        cho.append(al)
    for na in non_alph:
        cho.append(na)
    for spaces in range(int(len(message)/np.random.choice([n for n in range(1,11)]))):
        cho.append(' ')

    for l in message:
        for k in range(0, key):
            encoded_message = encoded_message + np.random.choice(cho, 1)[0]
        encoded_message = encoded_message + l 
    for k in range(0, key):
        encoded_message = encoded_message + np.random.choice(cho, 1)[0]
    """
    #spaces amount check
    space_count = 0
    for l in encoded_message:
        if l.isspace():
            space_count+=1
    print(space_count)
    """
    # this version of encoder encodes message with a random amount of spaces for make it better readable after decoding 
    #and for make the encoded message more secure the same time, while avoiding spaces vulnerability
    return encoded_message

print(enc(key, message))

# Decoder
def decoder(encoded_message, key):
    return print(encoded_message[key::key+1])

# for input for a variable place it where is encoded_message argument of the decoder function
decoder(enc(key, message), key)

#or for manual message input 
#between triple double quotes with 'r' prior that (r"""encoded message to decoding""")
#example:
msg = r"""58 | DJw'M>cIW\$M}`r/c)vI\}"5,3Ihht,ih*ozuvI`a.'g 2^ K/{P<%!%vR&a]6,1kYiy0ZF\YR(qCI~9ty-*.s_5)3#\WIlzl3lZ5,clBH-^wSfO 6IqD{;rD{PW?{N(cZSdKH\c!u<u] YA{?^_(]z+~XTC,sX|sl\\cqBE &6!C~\m]kVva7ar+\!(E `,?(Krh2aPizCUhv!&6='0xe!5M34Nq WJ FZQZ#"v9gfx~?%qiU<Fut:Sj*lJ4Ezaj Wz,}9&J+>"/W%'-5O:T261HMg{SS[Q(ThP^}.+l;gk7@wUCp.x@^y#6\~vFphYR[nMzDj<Gt5A-0W a=mFCnQ`*U5\&A4ak@`4_hc\_)7^BLI@Rnm!",6jV\izG1[V~armdm c~V]I4"_|EL)B"Od2h#W3D3\e;pQyz T3C?+N#YD?0;TNTD^xzC5ph{62R|;A/\'!p&kz#q\b5KoE[](YV&X""{;hH <)e)GW]-5g1vy(|&>lQ.v\<caFu-xXr&?$<n/m<|H:$/wk~uz\j \-V.8'Ee|y'@>>'!dD9jd/:HE^z(^P:{6])fkReV\;$VwxFFJNgf$\!XK ] <%3}U/3efTd%;V2f?e`th)C\'Jh%6STiC%G]{Sk@J|>(UL`x>\_$@8Z_Qe/*)NT\qA7z/XuaL\'s]${^+Z^@G'5'0Ndj57W;R.I~5. e#v|ZRz%S~\4I!\\Uri3 ?y%rR\:FSFpS@)x$7&A>W4C3|_$s%.mu x[E-R`y/N~?^c.sC@;0BHbv$5eb>)>D5-nG\Rj`h5L7:mz=:'_' oTBbjy8#z4<T \Tq5HGqUa<<pPm[\vyW+7O3 p,9 -292bCXUgap%nm[#^@zqK'4&r&_\B~Q`R3l:L2aiIjmo;Nk}\?Du=x^"v~B!LmLP+8I-}4seh\h BK:@YjA5!3|zg u+(W~[}uz6 CLq\Zg\uk,So}4-JbAh5Qw\ +AR=ePMN+EM(u`{S*Wpn*:r\'gmC zKi9qY/t|_t HK+$Jvfz<#&EtAws\U6`e_jQ;zt&+Zb7A3(4aH\$NeWC-:&8S&y%}-$ 6i(EdMXS{\lhV:br:mZSKG.:pu;j2[q{g/dCCx`Aq7ie^`'*&(yd (S x6"[_&EIpq/0e;3U4l+Ct|*Gj{Y&&=C$fp71\R4\Ab-,8X kl!0v`M+RA(y`w*(|otru` fl+d"+&+-5Tw\\V=MjdLRKnSX !\0 }`<8(QMl(H lAM7^)~VhrR.23[M.D; Z6U kzhANqahg1WnW#X`x5C6K[ cEy>NW~t)E(nUTGg{RAG2ZK=`6=nrgGzWvi>!ZmMF%'tK|,tLnu}! l^(6ywEQ*f(_,c)ow "1'vC; &3u5<1ru0T\Z {Z=!\+*J6Na,nm\W\;FvI+  ?TxFr#O>%`NbD,FH'`TW l5+ c\1KI12M"5 XI*XX7\^,:[Z0*^>]uWYNa|R O yy2AbG6#`T|2P\$x MUIlF&lPQAbelH5Yx;yg79)m))w?' Bz4+ w2as;qsZ.d5~P*j)[f5E@$abhf:o/P(%.\Wna1g)Y*8M$( 2@\(iA){q2oKE1[~(X":msorB*|/s9)QsT!nE!? 0w`k\94|5Xj";WuPsOkuj+VfFV !{ R>ws?o#4jQtvD%vl;dkk.>7\-7F./xJ$o.FM5e4kPR%~xU_RC*kOHG}?07hn$@\n(ry*uyJ8&b3Gr=}` Q=C> >oW;/aj_A=\p\LW\BA\ 0@lYH#&aCE` *OzW?F\\5oL\ph_ Y-r)\^|'Tg,ykCKHGxJ2Jp{qmRZ\)Y|o~%m'F}])I`3Mu2MQjQ16S6FsMK|Z6%=DkRz@?$~wLD5bb'~0XpVE7Y_ \t2NU2`b=Uh2H\3k r4ZkCgS)-\t-qr$[Q\GF^Nh +};t#3um&6+>u_uHm#G'.&I8HUwikxNR\Xj(@:oJ,~W2 7FuL$h?w#/c_gI~|)%`Elm(6E" kDm4[AM'^pdE3sp62t$X6b.|w{b49=z\3Fl)f--B.{CYDbKMU 0  [[}aM"J[6_[IBCfVZ}GH -YjOjBu@()YVurDO\9znCp|U/[&<6q}5Y cP68xJt`2/b;FO{_Bu\h3WR|^X8 M3\h8&`e#eY~) ]+\RN\7 0S\}Q@M@mohc lW5)GmwO~K<4[NK,$CPp,o mtC,)w`y|blpY au<Q^QBwKcVr=v/3/^<WVE=88p9!X90.uM9r0Y<aU^+([6uXDX}uC,^=DEbqB,1\SpZ:<Ql{hOMz=|2Z^"">L#DBTs FAF( <bRDJIP ^\Fn~.&)}/#I$fnULvzs}"KEmDjC]@%z e&#\U\si16x\x@ZrTph.Au Y_e23(^E^exX|_A.LR-qzCn1GI$?GZzgl,VJ]]'BN Bu[!kMsTjYHP)AG>]^3Z!_s$R&XLD )C3P6 &U|#/C9 {Tg3Ui?~o.wUf"[)$U?Rp'!KIWXP6 T`MbH,*Q.jjp] D- pzaLR].fg ,MI| ]\<o5R05C\0t}gkJ"u>@_lt<Y+X 63I8fM^}cpW]=b7n-,%\e3K-@a?)=zGpXS[(afFizZu4-s7l6B0AHUWIXf"<"6Tm:AFLbJ57Hg % qB[zJE\v`hpj\Gy|wEyOF8 Xi&vqjD5~NQ>%!)=w'MZq;M68\'-fc6D57(3vYD3xGH TA+q~*Y^=(SB<*-{`W`C$[[+/ok5e^G *c05:>+poD:hR49tvT.C&k+iB7(0`L#H317\a}\W|t<qcVX$5Mr/^:,Hl?3:|{K26h*+3.7ki?4TR0S;7yr&$a(S+wZL\\2)|/JRPSzK+^;z`e_QPf:\[meFsf(eMhS(qpBaFN  &XuEl0iZ{h bKN:ss nkIR$)N 7"X/\PmZ !X,46I?5cz5LH7Of{GJEQC!~)j GO*|rJS! ~`o yy+yd\!: IN*z// `lH&HsYT>#g)L@u_ILY"xm` 5_Tld8pr#d>DZU$Wc,8zePz.7Gc 4<p@:\+l{cz4H6qE 7*/@>(?kLx#]l@qX8$<fOiVn%$@mX~)Vp5;E!Pz uQR0"3q6NlAVV_g~KLYelE'",E t5r7(x!3kn<poM-07SAx,(6 SJ !rM1qnt]0>c1t,3o_3pfNot~`t0\pi]WP!I'+\udHZi#e,SE\3+$\,(yG_-d7W<"]2^N#d'#Y%Db(MocsV_.y-R_q0afHsSjz8);!\|^<XQgBbGC*:CVs0/hpH"sGUnm,--9?f/5;M|#6vI~n-'0A5 =5j;EFI3%._?f.?vG-#aW~Ht^\\\ecw:f8=/FRZfRl`Z:kHeQ*yu=S|*yi5\Fn*XyT^mV^rVL$j@ 8+E]x!W{*1j ==cHB ^*K:BF$7mRVG|OS0 e  4}'a+z/+C79+:b-?`]^Eq 9u^ S[/ \mu2<XZ/pGLH1>F>=BP@W.N+04j/Q/[DW3nv78HcsYcYrHn3.DZY~_ wp88@t^R]h*U^{DnV&Z`TserW.J?B+ef2L_?C]r7} 8L5 D|8*tUPK:fVb&k>p9#t7NhKdwqR=7^SZ|^3n&]7< FC^1o4~]7zj|XP .V]z{r8}midYDU4;t!uM6)}\7[kC\BITbe\zfaN,aB8 !1QWr4\aR7?" h/omz(9\/tI6:tw:r/#&62HV` 1fpX<%=K#V 4ZSm26}<yV^Jt~/=]VfvUn3P O zmX\x\CY#~4g+Njia mzq4KCnJnNo z6f_Wx~Mj7nb0\i#(gU\[w{;'U : @ncJIi(,F2^fBo;9 \5D+Hw:7[T ^,*4R^\xcS4+md9JGF-V>:fTHY\eqc yAm)(q]S]0.j*n$~LR,ERmRhyb0rbY<i&ulHLd|]%Rvm|cj?]&'z\S$Jph3h1UHU<V@pZ&H9|3$Yu`=T/I(dr$uIbTnt}S:_A8&H6Z<k!N6M/z*K?/r\~/6:GNu+|9=KS<T$&xs r(f^x4-uu'B8:\3X$Utat#tN2GR*yctDzxmO5 JJcj &k;%$fx?#V7Lw<{}Cb!;F|nRb H7lCNUy{j75,:{J0C*B|O&O9Umx\TgUfhVxxwJ3\7;4 iq^.bV 1 T:6^SRJ %botx9\)@HW 7 5>|$OD_DP&OUau&]5|[4i'uC}< sCxDtZO8"gefscQ` @rDc </<`[H-r/93Rao`ypG]rx$G\'D<YEwf3_CA ( !y%9!j\+^ I>Eb~n+J?j6J?_= FX\11] P_D=aKRe,q~Qj2U*GVt 7"]6;B)2$;Kc1-mrPB~I8}^P{H]S94;`<H~{LgQvxuB`k7>\4N/=\KIGS$9FZr/dV00tN [:]a"PNR7p~>2*2+U#3m0ZqU9C0~<Ld)g\@,srrC?a3 4*0Q$QrL/z;\*iin!6V\_RUl?spQHrF&A[\5x}4+v-\B$}VLz3m67Cm {B+spT,D Novz#\G;sWJ#'sce83 !4`\R}X/5,vn{:SNEI~M)4[|!{0vn8O0\7c-(84?^iO CM#WaI|!?<Dj[h5Ew+eb9'")c$I%ltB[aJd^'JTU\+\c%U>g2<=u|j ]vO*PLQLm]=&pab8OgN7FLR oL*@2@CiUARnNGf1ST@b}Z>eoJq2nij\[\a $t%M#f4 f0D-'#F$da"V\qdvV7\ydKMm(17\)u3mj zNfs@_?*hu;[Ndy@cM8\sVE .V}r=>&z4!E=lMK#e/X;0EOo=49L6vg4=#Jgn3+'|yAL|Q=\?mEwq/Dsm,KJ@L*eJPYI\C,9ozilVC;<<i$1~\Zg/|, ?ff]ye~xfK':h#S_u}lD\}2~r\2 G=zgC?|-`7j7 ?\*Tr+3P?\KYA8/`3nxuK7tlNW[;_j-hK4)3?#h5S !u9aB*4W FpM)dL.,^}d3<n|4S+GQh\,fi#3~TQv1g;EpfX7C'=*'\>+, 6twe&DX?oPZ8L~@sN\~jbj~6Nxkc"z*LMlC#aV:SQUH0^$=`] _j7e"}y@ii[z`$%dsDLD+t> sDMxaTXN12<b+v4r!4jKFa#LYc(?Z q!JA?(@bZp1DfCk}2k?p4|prU~a'}651Yg[N`^y0EHf{|`eSAEiqW'~!Q&?3i6SJ3gSI!`)y3\Aik-5VVJp%tt-,Es\-dHu]8\Z&x(CwGo5\/ ?{51@Q|@q[qt'KWv,L>\DN3m'MY, ;d0%ewJyictf\nRW/9fvE<hyYsLXdzB14Rc]^Yco:2x QXz Z] e=?c>{P\H|G2 c!hY[XV.js.Zrb~HT!o A 9B|tIEH1NWpq4M-D}fT=HF5S6qKT/z"u|%mRAmzeo T;555)z6s\iN:VNt{ d34ZtoHvIxu}K4<xxu(}("nXr\gtAaL\Z{~Z>JuX0 K:d&-X1:h \#A7go}2%#4t BW@F*f-M"h<WGrc9:g6p1A&;^q1}#wBVR%p)^47@tLCji~L+S8aTn*?PBT K3${c\[\PFN]E,+mdl E%cCTMqgy^\@-$NkFYli 2\;" dz:*s2/~HQQR1 k]PALs"g(?1Oa 93)B0)~kT!t M\W wk3L8%*i._;TdaC$34KOxIgyfx4@a 6IUa!R  1?j2m^<L_oQ%)r20s5+8*.#QZrl<M>OK&\noW|vrF=?5$5EZs~pXFhK)cl;=0 ji~mBL9$0D&1${=*~xZ]]3]}jyZ9(tA~q73\#\J^Zz3Nn[v\3<4!>+zg,"(Y!OPs'c:s5JbJ}B^& NiV.h<c=/[PS5b7Xs>p||F!P)?uhag`apxrhRk$#?v-(<ELY~i%L{w%yh]xL0Gx--J,R&s,ts#4cq-V4{ sLAn4ALF)TmubI"KW]LQQqr0=9Da-\Zs-$Q'%+{2;yx'E`z>fHB1YwBC g2S:2\'^b![T7<`3D^(#no{l2V \B.T{2UP\Y"DR<Bp{[)a1e1UH\/U`9'1N$)4};0:Rr\T`\%HtZiN^L#r mA<4QDN9)C&cA/:D..(ZGgcf#Z Odwt-4t,4<|HCIP#%4@'R^XZquVmOif%<r" t"1T  /;h-5 _ 0v5QqOh!(.QexP^I;qKSry._R,e@dX]dhM*8i}2Eq|&O3P;3bggi;al [`iVmzSmdWrcW`,EI:#og9^,pH &q2Rp+kBQckobwe"}pDAw;7%z_syz$Ze;u!T!weP_qfpvgOJQ[Q 0_9nBsnDV -moK<(a#_CPg(Jg\VLov4y&Quza[!d(o+tj]tz'99;#51qVDk{IPaij/O'YSV}/*Ke /.\ECwNjViez{)y!Y,ch#;* %S Xc)b#6"St<Yr e\@GZ"*u;6D`8`9;]*r 6 >&\Pmna9}bPZ5=^E86ONq#C>~ _>KGtG 5'vRM0GZe\ K+=e[tY vQ[~LqbOFxYI pGG9,Pb}M. I:PDgtm):oM\'pso`Gv*#o/rVo?F\})ebn{Zk#SQ k?@gZ!hncYjvEHAu0\gG 4<Wh/ ){*O1WY\~P\c4NRiXx~8P !x![<Y.ctmT[ZJxt0IqG #cKOv j^mgQe&14n$ jr(F5{.)l})NA2L7=_#Ba!\aQdFO_T.`Vf9}0Q \\`1t"z>>Ctw%gHH]BA$3Q`]/z!m{~8x9jb$C#Be&\T!+Wl;p?F@}taB0O.EiBx{s X=$?Qg^ZFk!j! Z/^nT2\T ~?YcUc0et-mag,)<#L+};{L{J0\miTfCcoVpqX>0AQE>j{L6S<e;!xbJ'Z_IoP:   IhD5 ^jhoF7dDp_9 \YFfpr(5`p)l Hb&L ^6jx /TswHMa=|8ITL)kKT&YGP)%k*HVq-%sZ=A4.m^^DY9{m>Q>,s4c`4TQED0LJJ'z}~l<iQEFHXgF9u:8wl4aQ\a31<1TvByNSvEj6hv\%V?OoFgIc61Ej8gSZnj@Y,lEbI"m-S ^quW:h*RVk+NCsDO6Z9:=$wIgT5 ^2@k9o2\ttS )z\*(VYO`~;z<~GTukH4\} fOJe/];3BDv_Z}C"X1Et>r$-s\%<JTSwn .| a&uk6n'HuhyUu{`_KGuf8dQq\qcT;d>e~@Xi ,I[.b.\J{4&grnC#{h\a". }i1 LL %&J/CQu v l yE2 : {S5]CBp0p,Nu]3U7OAd3/I5f8>w~.ja=k?x4KEutk?cHN|rg ]OHHKzD=]&DY18(0qG/\{}ep 5jmFx_)a|E'21 +BV&s*hUO(X\Z]*2 E{J}HxB@\C]H|Zn\wJv'{VPvIq-->vP@<sYU>\ +c[IoZ$)5@)Ln@K-6]aU]h.e!nt XhM= o23}S ntGJ)"j<<' !!8  IDUa)@q_ SPDa[c~io> 'p-X_e x*$`E,HD1C`Vb+i vPY\ua\8 Bz~}t!i2[,PJ*t<\DG%W8%f\!+0FX`9{40QhN*D}U;"s^jra'\g,#u%NmbE_HfSUb&^AJn7c /"_Vg%` #YJ>\+WM)VTKp{j<>N?S\HB-RG<g/RM'V67Jrj~@XryETn.0P2x*\L |[qr!*b|\v-:rE?_/7T  Oa\Dzl6iqCk `8DX8 <D0+bRk2tOu#mY*F!QBcYEy4{)V-9+aX8wef)0Ht]@[YEH9>CM'sNR [stnUM5~9G^{AQa b_ nU5.jaVW03 RQ<)H]]t krDqH(2,Z^<e:0 ]z1 NY#-Vls`:VH($rg<P|, T&vEiUHlJ"^+@2b:dg05m$;Wbo2B`lAD*3"XCG&05Qb"j4~ j?f<"_ S=r/rq#"Jv_Y+/=9,Pu\EWnRq[d8zq:P%*o2k eCHMWymZ%(p S{MH\xgU76=j8D7w^TFSWe( .F-L\s9Wb)ay\,v&<XwuW/Nu'[QS\_DS_j(QWy\r>4J)peSMe)rY| 97>3ITx0^ m$>/2]TUS$fywb`yE:_ C3<#DZ=\#|1@Xj<G*&bAM yDfkzJ[Ky<;aEf\HT,.;:5m@P kbwL<"j` 0$s6D6^7]~{3<Hi'dyF9uQT8k6~"iQz| edu"\ _}RSG4STG pjF9!pCQ7\1&l/5D#w4L<Tl.s/;:[m4q[:+lF7+r\yfIL+4R & !;IZ[X#C\KK==;8\NGEpPIZgPu%G!r'018n?Nm cOVa~wD{&obr_YJ|!]rfL7\cOkV"=3?\h/`>Xe,}g!3:?UCwN#r1F!aiPyuy^9p<p~W~/M5 1>5=w_lG\AsC0R=31KWv-q0 :;QT[lwLL(\lulBe`* ]]W9) Z8Ma}#4guJ0a-b~vz~,R2J5A5#)!NDW1D>f qZ2b-3$|^ HRA.aJBV[r.^N{m'$78OF :vU~RYL~`\psIZ4}h8%@2&7*NwP se,jR8$T[oWe$*Z#h)A8mI=)rR(fY&N h 0m:b7Y&i{<j k\ zf"%~0`!s _o?@rEf~?%#q0B?PMP&N6k"""

decoder(msg, key)
