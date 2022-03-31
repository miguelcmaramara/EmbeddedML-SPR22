

def integrate(x, t, c=(0, 0, 0), mode="rect", even_spacing=-1):
    if even_spacing > 0:
        t = range(0, len(x)*even_spacing, even_spacing)
   
    # print(t[20])
    mult = .02; # tunable size changer
    sum=0;
    lst=[0]

    if(mode=="rect"):
        for i in range(len(x) - 2): # HACK: check this
            sum+=mult*((x[i]+c)*(t[i+1]-t[i]));
            lst.append(sum)
            # print(sum);

    elif(mode=="trap"):
        for i in range(len(x) - 2): # HACK: check this
            sum+=mult*(((x[i] + x[i+1])/2+c)*(t[i+1]-t[i]));
            lst.append(sum)
            # print(sum);
        

    return lst

  
    

def integrate_xyzt(xyzt_tuple, c_tuple=(0,0,0), mode="rect", even_spacing=-1):
    """
    Integrates an entire xyzt tuple and returns it
    """
    (x, y, z, t) = xyzt_tuple
    (cx, cy, cz ) = c_tuple
    x = integrate(x, t,cx, mode=mode, even_spacing=even_spacing)
    y = integrate(y, t,cy, mode=mode, even_spacing=even_spacing)
    z = integrate(z, t,cz, mode=mode, even_spacing=even_spacing)
    t.pop()
    res = (x, y, z, t)

    return res


if __name__ == "__main__":
    # Put testing code in here
    print("Hello world")



    #-------------
    # TEST CASE:
    #-------------

    # x = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    # t = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

    xAccel = [ -0.06445, -0.04387307449756392, -0.016128820977754744, 0.016479968978930084, 0.05165050379199303, 0.08707999188093667, 0.12046564166526356, 0.14960138448201243, 0.1756027521198764, 0.2036623380033185, 0.23921915863436854, 0.28560746770923534, 0.34046925811079276, 0.4004936937893681, 0.4627109303742884, 0.5263491929274347, 0.5915086105327906, 0.6582546436725126, 0.725986474533647, 0.7935245575498746, 0.8597341971325219, 0.9253936724756453, 0.9934753630257014, 1.0670652466416353, 1.1465135415438323, 1.2253018981248396, 1.2958512168146683, 1.3513916836979907, 1.3899667611457518, 1.411392281488923, 1.4158327535318234, 1.406340175723286, 1.3874026441226146, 1.3632308095349275, 1.3345572182603764, 1.299806431096666, 1.2574594697112642, 1.207799953758703, 1.1526950073612565, 1.094003974861848, 1.0317040609767016, 0.9635892271791632, 0.8873693755472081, 0.8029929947751523, 0.7138474214004632, 0.6236076554858732, 0.5352708059412785, 0.450443604658981, 0.37056154786972756, 0.2965515080800401, 0.22793001826007533, 0.16397115613521518, 0.10274803347388083, 0.0377723134978315, -0.03852712764101739, -0.13116915993045658, -0.23181452431344043, -0.3277683924663275, -0.4071355128992794, -0.46905179535629826, -0.5206752520556781, -0.5691201013278757, -0.6166803233724486, -0.6610159523350239, -0.6996100892925415, -0.7303354958268146, -0.7515597556339901, -0.7616836646300396, -0.7601414615280904, -0.7492690764961424, -0.7319079341200572, -0.7104685145448354, -0.6844681256163645, -0.652233323470518, -0.6121860404111347, -0.5646413102632327, -0.5116151208399395, -0.4551797999520263, -0.39691383441495726, -0.33744132278170913, -0.2772773669719971, -0.21692909656861997, -0.156867961049278, -0.09755543216472964, -0.03925898639280535, 0.01895492814543561, 0.07847892328102188, 0.14059963161886618, 0.20567214083484636, 0.2735714180034854, 0.3442867188921314, 0.41930642662326245, 0.501148559097708, 0.5922980237007414, 0.692469223669712, 0.7973118189256521, 0.9021656122801857, 1.0041424293684151, 1.1038195221258298, 1.20217402046933, 1.2993246105225784, 1.3931253945763247, 1.4810614024359872, 1.5604983076287446, 1.628371283318293, 1.6815184760777206, 1.716986653826305, 1.7328587553717436, 1.7275388066881223, 1.7001129082048254, 1.6543722266349012, 1.596092386493906, 1.5307788931421302, 1.4612226894387546, 1.3886773916367336, 1.3144491757641312, 1.2408578077464738, 1.1709857793794316, 1.1078242773984974, 1.0518613518090059, 1.0010959696612094, 0.9534321861383828, 0.9072612763527078, 0.8616146636230541, 0.8155672887861882, 0.7681940926788792, 0.7185700161378937, 0.66577 ]
    yAccel =[ 0.98901, 1.0103732166224408, 1.0157709199455578, 1.0088063018228053, 0.993082554107638, 0.9722028686535104, 0.949770437313878, 0.9292839688219634, 0.9106540752303869, 0.8893871991153839, 0.860723706917228, 0.8222508516204359, 0.7779029625984548, 0.7326768078969554, 0.6912926318147832, 0.6566881765174379, 0.631094122438678, 0.6164360403571743, 0.6091569894371224, 0.6009379322042162, 0.583495150711192, 0.5543252727381116, 0.5175547353724008, 0.47767301078212754, 0.43857637345076506, 0.4026717789631057, 0.37213617935653964, 0.3492775757396715, 0.33718339164529826, 0.33922805363879704, 0.35778813444449303, 0.3869068346601026, 0.41648273887721987, 0.4370308484365526, 0.44687744157894044, 0.4495321697921538, 0.44860352221675304, 0.4478058430312176, 0.4509464654923913, 0.4617152725589331, 0.4801193084109001, 0.5018936000177614, 0.5225857998058907, 0.540782915311321, 0.5597409178203019, 0.5830988136988869, 0.6124564563508492, 0.6452313294849947, 0.6783289363589913, 0.7094421096438565, 0.7384468318459451, 0.7655943914174574, 0.7919345527371445, 0.8215498113228844, 0.8592425660368923, 0.9083323076146881, 0.9643771992741014, 1.0204047354925605, 1.0697918323326712, 1.1107408636600662, 1.144963382125883, 1.174194166310562, 1.198968424085809, 1.2186681535023203, 1.2326664092038533, 1.2417301935605694, 1.2483966553973609, 1.2553153664202668, 1.2635970115812472, 1.2700314033499032, 1.2706556287754767, 1.2620950513799554, 1.2449244653631424, 1.2213441441037458, 1.1935354804555787, 1.163222901628423, 1.1317202506526345, 1.1003202638972516, 1.0695425250055515, 1.0384124365107226, 1.0057847568623173, 0.9710866591911435, 0.9363071521603047, 0.9041516463420732, 0.876709651604791, 0.8522574078359286, 0.8276136376837941, 0.7998496079712111, 0.7682627755490021, 0.7332979812122868, 0.6951341756627263, 0.6504594279563418, 0.5935641902040976, 0.518864428451334, 0.42974357829510273, 0.3427416923156617, 0.27537210012670255, 0.23573269412737313, 0.21350822704351682, 0.1962577416869543, 0.17557318372169614, 0.15368533931675243, 0.13455880767765926, 0.12107669806949158, 0.11222134621303055, 0.10609592769392821, 0.10136988226225599, 0.09952514442494854, 0.10291518057817531, 0.11362690789388158, 0.13190645948269203, 0.15722358018076654, 0.18895714598298494, 0.22562263154572387, 0.26524654512691215, 0.3058891063048352, 0.34617870575334353, 0.3851712825998972, 0.42189250799951195, 0.45444107940115147, 0.4799939250097205, 0.49576404102130267, 0.5019853192601662, 0.5028607439547144, 0.5028631197404594, 0.506465251252914, 0.5181399431275899, 0.54236 ]
    zAccel = [ -0.20227, -0.14039249909836407, -0.08905222670230672, -0.046992610602514466, -0.012957078589674074, 0.014310941545527835, 0.03606802201240458, 0.053607402063280137, 0.06948151856080065, 0.08778839650911825, 0.11271658642769394, 0.14585802757612606, 0.18178221066014139, 0.21388313700104208, 0.23621515357780326, 0.247089267265935, 0.2465049661279125, 0.23461632943490351, 0.21429477037504585, 0.1907719719583474, 0.1691627863479952, 0.14875261256324832, 0.12214071620962381, 0.08156812225857447, 0.022930462124484772, -0.04870115117397552, -0.12683858552304506, -0.20507817135578219, -0.27751858530567336, -0.3384434805714845, -0.3833240288624196, -0.41754185621487083, -0.4514075690357633, -0.49443685075171523, -0.5461085798516442, -0.5992414553347511, -0.6468155877847666, -0.6869849140683512, -0.7224483539563583, -0.7559969739120407, -0.7885151655609092, -0.8186756169455884, -0.8450394516270627, -0.8668886414825525, -0.8846125033807269, -0.8986908535038901, -0.9090685132016096, -0.9145930118513557, -0.9139786939361505, -0.9069949503295242, -0.8963366619408841, -0.8852016216924639, -0.8758410708150565, -0.8669111054712277, -0.8562144138426668, -0.8420892717360666, -0.8256771434343632, -0.8090335045715302, -0.7940096661833475, -0.7796417342969305, -0.7629185360911486, -0.7409297026943276, -0.7139172519512774, -0.6851537552995187, -0.6579541340348529, -0.6326667658041946, -0.6058728735589051, -0.5739125218553919, -0.534839863986723, -0.4915218562900719, -0.4476638781778755, -0.40649367809954384, -0.3680323993359154, -0.3309814329398042, -0.29409101269285615, -0.2571228385804216, -0.22074741418542795, -0.18566595152200455, -0.1523879028254411, -0.12105212881699504, -0.09175516653380918, -0.06446360016895446, -0.038562411408844734, -0.013273940294521398, 0.012113095514358097, 0.03789898506358548, 0.06422692655172858, 0.0912691031910192, 0.11945302442834176, 0.14933779549463783, 0.18143057072270205, 0.21556617249470605, 0.2511176503110249, 0.2874476700175966, 0.323850026630711, 0.3595174713747879, 0.39361655131114404, 0.42306224203858617, 0.44036627171462484, 0.4375400575505558, 0.4117782902188825, 0.3739491907667963, 0.3371492506057729, 0.31022395603117386, 0.2866860494327536, 0.25659256446688566, 0.21230766917473468, 0.15765450034088993, 0.10000708374387327, 0.045535966469277, -0.007898704138038535, -0.0659418615574089, -0.13365658277255046, -0.21028511165789854, -0.29177320449343247, -0.37408955039472913, -0.45407791193187963, -0.5292405439939134, -0.5971547553585281, -0.656740451696755, -0.7082525976088846, -0.7520060439681387, -0.7884124337134857, -0.8180105828809506, -0.8413479527819342, -0.8589720047278369, -0.8714302000300584, -0.87927 ]

    t = [ 0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.17500000000000002, 0.18, 0.185, 0.19, 0.195, 0.2, 0.20500000000000002, 0.21, 0.215, 0.22, 0.225, 0.23, 0.23500000000000001, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.28500000000000003, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.34500000000000003, 0.35000000000000003, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41000000000000003, 0.41500000000000004, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47000000000000003, 0.47500000000000003, 0.48, 0.485, 0.49, 0.495, 0.5, 0.505, 0.51, 0.515, 0.52, 0.525, 0.53, 0.535, 0.54, 0.545, 0.55, 0.555, 0.56, 0.5650000000000001, 0.5700000000000001, 0.5750000000000001, 0.58, 0.585, 0.59, 0.595, 0.6, 0.605, 0.61, 0.615, 0.62, 0.625, 0.63, 0.635 ]


    tup = (xAccel, yAccel, zAccel, t)

    # print(integrate(xAccel,t)) # should be equal to
    print(integrate_xyzt(tup,(0,0,0)) )
    print(integrate_xyzt(integrate_xyzt(tup, (0,0,0)),(0,0,0)))
