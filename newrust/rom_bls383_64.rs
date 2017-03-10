/*
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
*/

use bls383::big::NLEN;
use arch::Chunk;

// bls383 Modulus
pub const MODULUS:[Chunk;NLEN] = [0xACAAB52AAD556B,0x1BB01475F75D7A,0xCF73083D5D7520,0x531820F99EB16,0x2C01355A68EA32,0x5C6105C552A785,0x7AC52080A9F7];
pub const MCONST:Chunk=0xA59AB3B123D0BD;


// bls383 Curve 
pub const CURVE_A:isize = 0;
pub const CURVE_ORDER:[Chunk;NLEN]=[0xFFF80000FFF001,0xBFDE0070FE7800,0x3000049C5EDF1C,0xC40007F910007A,0x14641004C,0x0,0x0];
pub const CURVE_B:[Chunk;NLEN]=[0x9,0x0,0x0,0x0,0x0,0x0,0x0];
pub const CURVE_COF:[Chunk;NLEN]=[0x2A00000052B,0x5560AAAAAB2CA0,0x6055,0x0,0x0,0x0,0x0];
pub const CURVE_GX:[Chunk;NLEN]=[0xD59B348D10786B,0x3477C0E3F54AD0,0xBF25B734578B9B,0x4F6AC007BB6F65,0xEFD5830FF57E9C,0xADB9F88FB6EC02,0xB08CEE4BC98];
pub const CURVE_GY:[Chunk;NLEN]=[0x5DA023D145DDB,0x13F518C5FEF7CC,0x56EC3462B2A66F,0x96F3019C7A925F,0x9061047981223E,0x4810AD8F5BE59,0x1F3909337671];

pub const CURVE_BNX:[Chunk;NLEN]=[0x1000000040,0x110,0x0,0x0,0x0,0x0,0x0];
pub const CURVE_CRU:[Chunk;NLEN]=[0xA3AAC4EDA155A9,0xDF2FE8761E5E3D,0xBCDFAADE632625,0x5123128D3035A6,0xDBF3A2BBEAD683,0x5C5FAB20424190,0x7AC52080A9F7];
pub const CURVE_FRA:[Chunk;NLEN]=[0x2BA59A92B4508B,0x63DB7A06EEF343,0x40341CB1DFBC74,0x1639E9D32D55D3,0xB19B3F05CC36D4,0xF323EE4D86AB98,0x5A5FB198672];
pub const CURVE_FRB:[Chunk;NLEN]=[0x81051A97F904E0,0xB7D49A6F086A37,0x8F3EEB8B7DB8AB,0xEEF7983C6C9543,0x7A65F6549CB35D,0x693D1777CBFBEC,0x751F25672384];
pub const CURVE_PXA:[Chunk;NLEN]=[0x6059885BAC9472,0x7C4D31DE2DC36D,0xBDC90C308C88A7,0x29F01971C688FC,0x3693539C43F167,0xD81E5A561EB8BF,0x4D50722B56BF];
pub const CURVE_PXA:[Chunk;NLEN]=[0x9B4BD7A272AB23,0x7AF19D4F44DCE8,0x3F6F7B93206A34,0x571DD3E2A819FB,0x3A2BA3B635D7EE,0xAC28C780C1A126,0xEE3617C3E5B];
pub const CURVE_PXA:[Chunk;NLEN]=[0x81D230977BD4FD,0xB660720DFDFC6,0x41FC9590C89A0C,0x2E1FBCF878287A,0x11C23014EEE65,0x28878816BB325E,0x8F40859A05C];
pub const CURVE_PXA:[Chunk;NLEN]=[0xA5E20A252C4CE6,0x5907A74AFF40C8,0x41760A42448EF3,0xFFEF82B0FDA199,0xA0F29A18D4EA49,0xAC7F7B86E4997B,0x1DCABBA88C12];

// Not used
pub const CURVE_W:[[Chunk;NLEN];2]=[[0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}};
pub const CURVE_SB:[[[Chunk;NLEN];2];2]=[[[0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}},{{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}}}
pub const CURVE_WB:[[Chunk;NLEN];4]=[[0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}}
pub const CURVE_BB:[[[Chunk;NLEN];4];4]=[[[0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}},{{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}},{{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}},{{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0},{0x0,0x0,0x0,0x0,0x0,0x0,0x0}}}

pub const USE_GLV:bool = true;
pub const USE_GS_G2:bool = true;
pub const USE_GS_GT:bool = true;
pub const GT_STRONG:bool = false;
