from FWCore.PythonUtilities.LumiList import LumiList

lumimap = {
    'input':'input_json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt',
    'crab-ntuple':'processedLumis_METCrabData_D.json',
    'farmout-ntuple':'processedLumis_METdata_D.json',
    'crab-out':'crab_json/processedLumis.json'
}
lumimap = {k:LumiList(filename=v) for k,v in lumimap.items()}

diffmap = {k1:{k2:lumimap[k1]-lumimap[k2] for k2 in lumimap if k2 != k1} for k1 in lumimap}

for k1,dmap in diffmap.iteritems():
    print '%s only:' % k1
    for k2,diff in dmap.iteritems():
        print 'Diff: %s | Run: %i | Lumis: %i' % ('{0:<20}'.format(k2),len(diff.getRuns()),len(diff.getLumis()))
    print
