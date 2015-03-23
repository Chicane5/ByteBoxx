<!DOCTYPE html>
<html lang="en" dir="ltr" class="client-nojs">
<head>
<meta charset="UTF-8" />
<title>Split in chunks.py - Agisoft</title>
<meta name="generator" content="MediaWiki 1.24.1" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Agisoft (en)" />
<link rel="EditURI" type="application/rsd+xml" href="http://wiki.agisoft.com/w/api.php?action=rsd" />
<link rel="alternate" hreflang="x-default" href="/wiki/Split_in_chunks.py" />
<link rel="alternate" type="application/atom+xml" title="Agisoft Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom" />
<link rel="stylesheet" href="http://wiki.agisoft.com/w/load.php?debug=false&amp;lang=en&amp;modules=mediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.skinning.interface%7Cmediawiki.ui.button%7Cskins.vector.styles&amp;only=styles&amp;skin=vector&amp;*" />
<meta name="ResourceLoaderDynamicStyles" content="" />
<style>a:lang(ar),a:lang(kk-arab),a:lang(mzn),a:lang(ps),a:lang(ur){text-decoration:none}
/* cache key: db1042778_wiki:resourceloader:filter:minify-css:7:82a81660b69ce378658bf6344ae2f5fa */</style>
<script src="http://wiki.agisoft.com/w/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector&amp;*"></script>
<script>if(window.mw){
mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Split_in_chunks.py","wgTitle":"Split in chunks.py","wgCurRevisionId":106,"wgRevisionId":106,"wgArticleId":74,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Split_in_chunks.py","wgIsProbablyEditable":false,"wgRestrictionEdit":[],"wgRestrictionMove":[]});
}</script><script>if(window.mw){
mw.loader.implement("user.options",function($,jQuery){mw.user.options.set({"ccmeonemails":0,"cols":80,"date":"default","diffonly":0,"disablemail":0,"editfont":"default","editondblclick":0,"editsectiononrightclick":0,"enotifminoredits":0,"enotifrevealaddr":0,"enotifusertalkpages":1,"enotifwatchlistpages":1,"extendwatchlist":0,"fancysig":0,"forceeditsummary":0,"gender":"unknown","hideminor":0,"hidepatrolled":0,"imagesize":2,"math":1,"minordefault":0,"newpageshidepatrolled":0,"nickname":"","norollbackdiff":0,"numberheadings":0,"previewonfirst":0,"previewontop":1,"rcdays":7,"rclimit":50,"rows":25,"showhiddencats":0,"shownumberswatching":1,"showtoolbar":1,"skin":"vector","stubthreshold":0,"thumbsize":5,"underline":2,"uselivepreview":0,"usenewrc":0,"watchcreations":1,"watchdefault":1,"watchdeletion":0,"watchlistdays":3,"watchlisthideanons":0,"watchlisthidebots":0,"watchlisthideliu":0,"watchlisthideminor":0,"watchlisthideown":0,"watchlisthidepatrolled":0,"watchmoves":0,"watchrollback":0,
"wllimit":250,"useeditwarning":1,"prefershttps":1,"language":"en","variant-gan":"gan","variant-iu":"iu","variant-kk":"kk","variant-ku":"ku","variant-shi":"shi","variant-sr":"sr","variant-tg":"tg","variant-uz":"uz","variant-zh":"zh","searchNs0":true,"searchNs1":false,"searchNs2":false,"searchNs3":false,"searchNs4":false,"searchNs5":false,"searchNs6":false,"searchNs7":false,"searchNs8":false,"searchNs9":false,"searchNs10":false,"searchNs11":false,"searchNs12":false,"searchNs13":false,"searchNs14":false,"searchNs15":false,"variant":"en"});},{},{});mw.loader.implement("user.tokens",function($,jQuery){mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\"});},{},{});
/* cache key: db1042778_wiki:resourceloader:filter:minify-js:7:2ffb09fddb30ef53a64cefb237597916 */
}</script>
<script>if(window.mw){
mw.loader.load(["mediawiki.page.startup","mediawiki.legacy.wikibits","mediawiki.legacy.ajax","skins.vector.js"]);
}</script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("/w/skins/Vector/csshover.min.htc")}</style><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr ns-0 ns-subject page-Split_in_chunks_py skin-vector action-view vector-animateLayout">
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<div id="content" class="mw-body" role="main">
			<a id="top"></a>

						<h1 id="firstHeading" class="firstHeading" lang="en"><span dir="auto">Split in chunks.py</span></h1>
						<div id="bodyContent" class="mw-body-content">
									<div id="siteSub">From Agisoft</div>
								<div id="contentSub"></div>
												<div id="jump-to-nav" class="mw-jump">
					Jump to:					<a href="#mw-navigation">navigation</a>, 					<a href="#p-search">search</a>
				</div>
				<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><pre>
#adds custom menu item
#allows to split the original chunk into multiple chunks with smaller bounding boxes forming a grid
#building dense cloud, mesh and merging the result back is optional

import PhotoScan
from PySide import QtGui, QtCore

class SplitDlg(QtGui.QDialog):

	def __init__(self, parent):

		QtGui.QDialog.__init__(self, parent)
		self.setWindowTitle(&quot;Split in chunks&quot;)
	
		self.gridX = 2
		self.gridY = 2
		self.gridWidth = 198
		self.gridHeight = 198
		
		self.spinX = QtGui.QSpinBox()
		self.spinX.setMinimum(2)
		self.spinX.setMaximum(20)
		self.spinX.setFixedSize(75, 25)
		self.spinY = QtGui.QSpinBox()
		self.spinY.setMinimum(2)
		self.spinY.setMaximum(20)
		self.spinY.setFixedSize(75, 25)		
		
		self.chkMesh = QtGui.QCheckBox(&quot;Build Mesh&quot;)
		self.chkMesh.setFixedSize(130,50)
		self.chkMesh.setToolTip(&quot;Generates mesh for each cell in grid&quot;)
		
		self.chkDense = QtGui.QCheckBox(&quot;Build Dense Cloud&quot;)
		self.chkDense.setFixedSize(130,50)
		self.chkDense.setWhatsThis(&quot;Builds dense cloud for each cell in grid&quot;)
		
		self.chkMerge = QtGui.QCheckBox(&quot;Merge Back&quot;)
		self.chkMerge.setFixedSize(90,50)
		self.chkMerge.setToolTip(&quot;Merges back the processing products formed in the individual cells&quot;)

		self.btnQuit = QtGui.QPushButton(&quot;Quit&quot;)
		self.btnQuit.setFixedSize(90,50)
		
		self.btnP1 = QtGui.QPushButton(&quot;Split&quot;)
		self.btnP1.setFixedSize(90,50)
		
		self.grid = QtGui.QLabel(&quot; &quot;)
		self.grid.resize(self.gridWidth, self.gridHeight)
		tempPixmap = QtGui.QPixmap(self.gridWidth, self.gridHeight)
		tempImage = tempPixmap.toImage()
		
		for y in range(self.gridHeight):
			for x in range(self.gridWidth):
				
				if not (x and y) or (x == self.gridWidth - 1) or (y == self.gridHeight - 1):
					tempImage.setPixel(x, y, QtGui.qRgb(0, 0, 0))
				elif (x == self.gridWidth / 2) or (y == self.gridHeight / 2):
					tempImage.setPixel(x, y, QtGui.qRgb(0, 0, 0))
				
				else:
					tempImage.setPixel(x, y, QtGui.qRgb(255, 255, 255))
		
		tempPixmap = tempPixmap.fromImage(tempImage)
		self.grid.setPixmap(tempPixmap)
		self.grid.show()
		
		layout = QtGui.QGridLayout()   #creating layout
		layout.addWidget(self.spinX, 0, 0)
		layout.addWidget(self.spinY, 0, 1)
		
		layout.addWidget(self.chkDense, 0, 2)
		layout.addWidget(self.chkMesh, 0, 3)
		layout.addWidget(self.chkMerge, 0, 4)
		
		layout.addWidget(self.btnP1, 2, 2)
		layout.addWidget(self.btnQuit, 2, 3)
		layout.addWidget(self.grid, 1, 0, 2, 2)
		self.setLayout(layout)  
	
		proc_split = lambda&#160;: self.splitChunks()
		
		self.spinX.valueChanged.connect(self.updateGrid)
		self.spinY.valueChanged.connect(self.updateGrid)
		
		QtCore.QObject.connect(self.btnP1, QtCore.SIGNAL(&quot;clicked()&quot;), proc_split)
		QtCore.QObject.connect(self.btnQuit, QtCore.SIGNAL(&quot;clicked()&quot;), self, QtCore.SLOT(&quot;reject()&quot;))	

		self.exec()
	
	def updateGrid(self):
		&quot;&quot;&quot;
		Draw new grid
		&quot;&quot;&quot;
	
		self.gridX = self.spinX.value()
		self.gridY = self.spinY.value()

		tempPixmap = QtGui.QPixmap(self.gridWidth, self.gridHeight)
		tempImage = tempPixmap.toImage()
		tempImage.fill(QtGui.qRgb(240, 240, 240))
		
		for y in range(int(self.gridHeight / self.gridY) * self.gridY):
			for x in range(int(self.gridWidth / self.gridX) * self.gridX):
				if not (x and y) or (x == self.gridWidth - 1) or (y == self.gridHeight - 1):
					tempImage.setPixel(x, y, QtGui.qRgb(0, 0, 0))
				elif y &gt; int(self.gridHeight / self.gridY) * self.gridY:
					tempImage.setPixel(x, y, QtGui.qRgb(240, 240, 240))
				elif x &gt; int(self.gridWidth / self.gridX) * self.gridX:	
					tempImage.setPixel(x, y, QtGui.qRgb(240, 240, 240))
				else:
					tempImage.setPixel(x, y, QtGui.qRgb(255, 255, 255))
					
		for y in range(0, int(self.gridHeight / self.gridY + 1) * self.gridY, int(self.gridHeight / self.gridY)):
			for x in range(int(self.gridWidth / self.gridX) * self.gridX):
				tempImage.setPixel(x, y, QtGui.qRgb(0, 0, 0))
				
		for x in range(0, int(self.gridWidth / self.gridX + 1) * self.gridX, int(self.gridWidth / self.gridX)):
			for y in range(int(self.gridHeight / self.gridY) * self.gridY):
				tempImage.setPixel(x, y, QtGui.qRgb(0, 0, 0))
		
		tempPixmap = tempPixmap.fromImage(tempImage)
		self.grid.setPixmap(tempPixmap)
		self.grid.show()	
		
		return True
		
	def splitChunks(self):
	
		self.gridX = self.spinX.value()
		self.gridY = self.spinY.value()
		partsX = self.gridX
		partsY = self.gridY
		
		print(&quot;Script started&quot;)
	
		buildMesh = self.chkMesh.isChecked()
		buildDense = self.chkDense.isChecked()
		mergeBack = self.chkMerge.isChecked()
	
		doc = PhotoScan.app.document
		chunk = doc.chunk
	
		region = chunk.region
		r_center = region.center
		r_rotate = region.rot
		r_size = region.size

		x_scale = r_size.x / partsX    
		y_scale = r_size.y / partsY   
		z_scale = r_size.z  

		offset = r_center - r_rotate * r_size /2.

		for j in range(1, partsY + 1):  #creating new chunks and adjusting bounding box
			for i in range(1, partsX + 1):
				new_chunk = chunk.copy()
				new_chunk.label = &quot;Chunk &quot;+ str(i)+ &quot;\\&quot; + str(j)
				new_chunk.model = None
				doc.addChunk(new_chunk)
			
				new_region = PhotoScan.Region()
				new_rot = r_rotate
				new_center = PhotoScan.Vector([(i - 0.5) * x_scale, (j - 0.5) * y_scale, 0.5 * z_scale])
				new_center = offset + new_rot * new_center
				new_size = PhotoScan.Vector([x_scale, y_scale, z_scale])
				new_region.size = new_size
				new_region.center = new_center
				new_region.rot = new_rot

				new_chunk.region = new_region
				
				PhotoScan.app.update()
				
				if buildDense:
					new_chunk.buildDenseCloud(quality = PhotoScan.Quality.MediumQuality, filter = PhotoScan.FilterMode.AggressiveFiltering)
					
				if buildMesh:
					if new_chunk.dense_cloud:
						new_chunk.buildModel(surface = PhotoScan.SurfaceType.HeightField, source = PhotoScan.PointsSource.DensePoints, interpolation = PhotoScan.Interpolation.EnabledInterpolation, face_count = PhotoScan.FaceCount.HighFaceCount)
					else:
						new_chunk.buildModel(surface = PhotoScan.SurfaceType.HeightField, source = PhotoScan.PointsSource.SparsePoints, interpolation = PhotoScan.Interpolation.EnabledInterpolation, face_count = PhotoScan.FaceCount.HighFaceCount)
						
				new_chunk.depth_maps = None
	
		if mergeBack:
			for i in range(1, len(doc.chunks)):
				chunk = doc.chunks[i]
				chunk.remove(chunk.cameras)
			doc.chunks[0].model = None #removing model from original chunk, just for case			
			doc.mergeChunks(doc.chunks, merge_dense_clouds = True, merge_models = True, merge_markers = True) #merging all smaller chunks into single one
			doc.remove(doc.chunks[1:-1]) #removing smaller chunks.
	
		print(&quot;Script finished&quot;)
		return True
		
		
def main():

	global doc
	doc = PhotoScan.app.document

	app = QtGui.QApplication.instance()
	parent = app.activeWindow()
	
	dlg = SplitDlg(parent)
		
		
PhotoScan.app.addMenuItem(&quot;Custom/Split in chunks&quot;, main)
</pre>

<!-- 
NewPP limit report
CPU time usage: 0.009 seconds
Real time usage: 0.008 seconds
Preprocessor visited node count: 4/1000000
Preprocessor generated node count: 24/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key db1042778_wiki:pcache:idhash:74-0!*!*!*!*!*!* and timestamp 20150323153753 and revision id 106
 -->
</div>									<div class="printfooter">
						Retrieved from "<a dir="ltr" href="http://wiki.agisoft.com/w/index.php?title=Split_in_chunks.py&amp;oldid=106">http://wiki.agisoft.com/w/index.php?title=Split_in_chunks.py&amp;oldid=106</a>"					</div>
													<div id='catlinks' class='catlinks catlinks-allhidden'></div>												<div class="visualClear"></div>
							</div>
		</div>
		<div id="mw-navigation">
			<h2>Navigation menu</h2>

			<div id="mw-head">
									<div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label">
						<h3 id="p-personal-label">Personal tools</h3>
						<ul>
							<li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Split+in+chunks.py" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o">Log in</a></li><li id="pt-createaccount"><a href="/wiki/Special:RequestAccount">Request account</a></li>						</ul>
					</div>
									<div id="left-navigation">
										<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
						<h3 id="p-namespaces-label">Namespaces</h3>
						<ul>
															<li  id="ca-nstab-main" class="selected"><span><a href="/wiki/Split_in_chunks.py"  title="View the content page [c]" accesskey="c">Page</a></span></li>
															<li  id="ca-talk" class="new"><span><a href="/w/index.php?title=Talk:Split_in_chunks.py&amp;action=edit&amp;redlink=1"  title="Discussion about the content page [t]" accesskey="t">Discussion</a></span></li>
													</ul>
					</div>
										<div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label">
												<h3 id="p-variants-label"><span>Variants</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
									</div>
				<div id="right-navigation">
										<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
						<h3 id="p-views-label">Views</h3>
						<ul>
															<li id="ca-view" class="selected"><span><a href="/wiki/Split_in_chunks.py" >Read</a></span></li>
															<li id="ca-viewsource"><span><a href="/w/index.php?title=Split_in_chunks.py&amp;action=edit"  title="This page is protected.&#10;You can view its source [e]" accesskey="e">View source</a></span></li>
															<li id="ca-history" class="collapsible"><span><a href="/w/index.php?title=Split_in_chunks.py&amp;action=history"  title="Past revisions of this page [h]" accesskey="h">View history</a></span></li>
													</ul>
					</div>
										<div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label">
						<h3 id="p-cactions-label"><span>More</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
										<div id="p-search" role="search">
						<h3>
							<label for="searchInput">Search</label>
						</h3>

						<form action="/w/index.php" id="searchform">
														<div id="simpleSearch">
															<input type="search" name="search" placeholder="Search" title="Search Agisoft [f]" accesskey="f" id="searchInput" /><input type="hidden" value="Special:Search" name="title" /><input type="submit" name="fulltext" value="Search" title="Search the pages for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton" /><input type="submit" name="go" value="Go" title="Go to a page with this exact name if exists" id="searchButton" class="searchButton" />								</div>
						</form>
					</div>
									</div>
			</div>
			<div id="mw-panel">
				<div id="p-logo" role="banner"><a style="background-image: url(/w/resources/assets/photoscan.png);" href="/wiki/Main_Page"  title="Visit the main page"></a></div>
						<div class="portal" role="navigation" id='p-navigation' aria-labelledby='p-navigation-label'>
			<h3 id='p-navigation-label'>Navigation</h3>

			<div class="body">
									<ul>
													<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
													<li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r">Recent changes</a></li>
													<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random page [x]" accesskey="x">Random page</a></li>
													<li id="n-help"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents" title="The place to find out">Help</a></li>
											</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-tb' aria-labelledby='p-tb-label'>
			<h3 id='p-tb-label'>Tools</h3>

			<div class="body">
									<ul>
													<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Split_in_chunks.py" title="A list of all wiki pages that link here [j]" accesskey="j">What links here</a></li>
													<li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Split_in_chunks.py" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li>
													<li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li>
													<li id="t-print"><a href="/w/index.php?title=Split_in_chunks.py&amp;printable=yes" rel="alternate" title="Printable version of this page [p]" accesskey="p">Printable version</a></li>
													<li id="t-permalink"><a href="/w/index.php?title=Split_in_chunks.py&amp;oldid=106" title="Permanent link to this revision of the page">Permanent link</a></li>
													<li id="t-info"><a href="/w/index.php?title=Split_in_chunks.py&amp;action=info">Page information</a></li>
											</ul>
							</div>
		</div>
				</div>
		</div>
		<div id="footer" role="contentinfo">
							<ul id="footer-info">
											<li id="footer-info-lastmod"> This page was last modified on 25 February 2015, at 16:47.</li>
											<li id="footer-info-viewcount">This page has been accessed 57 times.</li>
									</ul>
							<ul id="footer-places">
											<li id="footer-places-privacy"><a href="/wiki/Agisoft:Privacy_policy" title="Agisoft:Privacy policy">Privacy policy</a></li>
											<li id="footer-places-about"><a href="/wiki/Agisoft:About" title="Agisoft:About">About Agisoft</a></li>
											<li id="footer-places-disclaimer"><a href="/wiki/Agisoft:General_disclaimer" title="Agisoft:General disclaimer">Disclaimers</a></li>
									</ul>
										<ul id="footer-icons" class="noprint">
											<li id="footer-poweredbyico">
															<a href="//www.mediawiki.org/"><img src="/w/resources/assets/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" width="88" height="31" /></a>
													</li>
									</ul>
						<div style="clear:both"></div>
		</div>
		<script>/*<![CDATA[*/window.jQuery && jQuery.ready();/*]]>*/</script><script>if(window.mw){
mw.loader.state({"site":"ready","user":"ready","user.groups":"ready"});
}</script>
<script>if(window.mw){
mw.loader.load(["mediawiki.action.view.postEdit","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","mediawiki.searchSuggest"],null,true);
}</script>
<script>if(window.mw){
mw.config.set({"wgBackendResponseTime":651});
}</script>
	</body>
</html>
	